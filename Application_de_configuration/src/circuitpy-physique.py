#!/usr/bin/env python3
import os
# for windows : don't write on console -> leads to an error with pythonw.exe
# if os.name == 'nt':
#     os.environ["KIVY_NO_CONSOLELOG"] = "1"
# kivy config import
from kivy.config import Config
# it's a desktop app
Config.set('kivy', 'desktop', 1)
# start with window maximized
Config.set('graphics', 'window_state', 'maximized')
# disable multitouch -> otherwise it draws an orange circle
Config.set('input', 'mouse', 'mouse,disable_multitouch')
# kivy components import
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.logger import Logger
# for process call (cp or copy) in shell
import subprocess

# file utilities for windows or linux
if os.name == 'nt':
    import win32api
elif os.name == 'posix':
    import psutil
else:
    raise NotImplementedError

# minimum content of code.py
codepy_content = """
# choix du capteur etudie
capteur = '{}'


"""

# content of code py for each config
config_content = """
if capteur == \'{0}\':
    import {0}

"""


class PopupMessage(Popup):
    """PopupMessage : display a message box"""
    def set_message(self, title, text):
        """set_message: set title and text"""
        self.title = title
        self.ids['message_content_lbl'].text = text


class CpypcApp(App):
    def __init__(self):
        super().__init__()
        self.drive_update = None
        self.configs = None
        self.micro_drives = None
        self.config_type = None

    def build(self):
        """app graphical startup"""
        # schedule drives update at 1s interval
        self.drive_update = Clock.schedule_interval(lambda dt: self.update_drives(), 1.0)
        # schedule config update soon after startup (0.2s)
        Clock.schedule_once(lambda dt: self.update_config(), 0.2)

    def update_label_infos(self):
        """updates the info label with number of configs and µCs"""
        s = ''
        if self.configs is not None:
            s += str(len(self.configs)) + " Configuration(s)\n"
        if self.micro_drives is not None:
            s += str(len(self.micro_drives)) + " Microcontr\u00f4leur(s)\n"
        self.root.ids['info_lbl'].text = s[:-1]
        
    def update_config(self):
        """search for configs files at startup located in the 'config' subdir
           and create a grid of buttons"""
        # search for files in configs subdir
        import glob
        if os.name == 'nt':
            config_path = '.\\configs\\'
        elif os.name == 'posix':
            config_path = './configs/'
        else:
            raise NotImplementedError
        self.configs = glob.glob(config_path + '*.py')
        # remove '.py' and path
        for i in range(len(self.configs)):
            self.configs[i] = self.configs[i].replace(config_path, '').replace('.py', '')
        # sort alphabetically
        self.configs.sort()
        # create a toggle button for each config
        for config in self.configs:
            b = ToggleButton(text = config, group='configs')
            b.bind(state=self.set_config_type)
            self.root.ids['config_grid'].add_widget(b)
        # update info label
        self.update_label_infos()

    def update_drives(self, drive_name_pattern="CIRCUITPY"):
        """search for µC drives 'CIRCUITPY' by default and 'FEATHERBOOT' for firmware"""
        # search for drives
        self.micro_drives = []
        if os.name == 'nt':
            drives = win32api.GetLogicalDriveStrings().split('\x00')[:-1]
            for d in drives:
                try:
                    volume_info = win32api.GetVolumeInformation(d)
                    if volume_info[0] == drive_name_pattern:
                        self.micro_drives.append(d)
                except win32api.error as e :
                    Logger.warning('Win32api Error {0} : ({1}) {2} for drive {3}'.format(e.winerror, e.funcname, e.strerror,d))
        elif os.name == 'posix':
            disk_info = psutil.disk_partitions()
            for d in disk_info:
                if drive_name_pattern in d.mountpoint:
                    self.micro_drives.append(d.mountpoint)
        else:
            raise NotImplementedError
        # tell what was found
        Logger.info('Drives : {}'.format(self.micro_drives))
        # update info label
        self.update_label_infos()

    def set_config_type(self, button, state):
        """react to config button change and update label"""
        if state == 'down':
            self.config_type = button.text
            self.root.ids['choosen_config_lbl'].text = "Configuration choisie: " + button.text
        else:
            self.config_type = None
            self.root.ids['choosen_config_lbl'].text = "Configuration choisie: "

    def perform_config(self):
        """verify conditions and call config_main if ok"""
        # can't go if no config is selected
        if self.config_type is None:
            p = PopupMessage()
            p.set_message("Erreur de configuration", "Veuillez choisir une configuration")
            p.open()
        # it is useless to go if there's µC
        elif self.micro_drives is None or len(self.micro_drives) == 0:
            p = PopupMessage()
            p.set_message("Erreur de configuration", "Veuillez brancher au moins un microcontr\u00f4leur")
            p.open()
            
        else:
            self.config_main()

    def config_main(self):
        """main function to apply config (does the real thing)"""
        try:
            # iterate over drives
            for d in self.micro_drives:
                # slightly different between win and linux
                if os.name == 'nt':
                    f = open(d+'code.py', 'w')
                elif os.name == 'posix':
                    f = open(d+'/code.py', 'w')
                else:
                    raise NotImplementedError
                # write code.py file
                f.write(codepy_content.format(self.config_type))
                for c in self.configs:
                    f.write(config_content.format(c))
                f.flush()
                f.close()
                # copy configs files
                if os.name == 'nt':
                    subprocess.run('copy /Y .\\configs\\* {}'.format(d), shell=True, check = True)
                elif os.name == 'posix':
                    subprocess.run('cp -f ./configs/* {}'.format(d), shell=True, check = True)
                else:
                    raise NotImplementedError
                # tell everything's gone right
                # TODO: how to verify
                p = PopupMessage()
                p.set_message('Ecriture Ok', '{0} microcontr\u00f4leur(s)\nsont configur\u00e9s pour {1}'.format(len(self.micro_drives), self.config_type))
                p.open()
        # react when copy is not possible
        except subprocess.CalledProcessError as e:
            Logger.error('subprocess copy : unable to copy ({0} : {1}'.format(e.cmd,e.output))
            p = PopupMessage()
            p.set_message('Erreur \u00e9criture', 'impossible d\'\u00e9crire la configuration')
            p.open()


if __name__ == '__main__':
    CpypcApp().run()
