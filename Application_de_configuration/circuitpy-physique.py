#!/usr/bin/env python3
import os
# for windows : don't write on console -> leads to an error with pythonw.exe
os.environ["KIVY_NO_CONSOLELOG"] = "1"
# kivy import
from kivy.config import Config
# it's a desktop app
Config.set('kivy', 'desktop', 1)
# start with window maximized
Config.set('graphics', 'window_state', 'maximized')
# disable right click -> otherwise it draws an orange circle
Config.set('input', 'mouse', 'mouse,disable_multitouch')

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.logger import Logger
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

    def when_opened(self):
        pass

    def set_message(self, title, text):
        """set_message: set title and text"""
        self.title = title
        self.ids['message_content_lbl'].text = text


class CpypcApp(App):
    drive_update = None
    configs = None
    micro_drives = None
    config_type = None

    def build(self):
        self.drive_update = Clock.schedule_interval(lambda dt: self.update_drives(), 1.0)
        Clock.schedule_once(lambda dt: self.update_config(), 0.2)
        
    def update_config(self):
        import glob
        if os.name == 'nt':
            config_path = '.\\configs\\'
        elif os.name == 'posix':
            config_path = './configs/'
        else:
            raise NotImplementedError
        self.configs = glob.glob(config_path + '*.py')
        for i in range(len(self.configs)):
            self.configs[i] = self.configs[i].replace(config_path, '').replace('.py', '')
        self.root.ids['config_spnr'].values = [c for c in self.configs]

    def update_drives(self):
        self.micro_drives = []
        if os.name == 'nt':
            drives = win32api.GetLogicalDriveStrings().split('\x00')[:-1]
            for d in drives:
                try:
                    volume_info = win32api.GetVolumeInformation(d)
                    if volume_info[0] == 'CIRCUITPY':
                        self.micro_drives.append(d)
                except win32api.error as e :
                    Logger.warning('Win32api Error {0} : ({1}) {2} for drive {3}'.format(e.winerror, e.funcname, e.strerror,d))
        elif os.name == 'posix':
            disk_info = psutil.disk_partitions()
            for d in disk_info:
                if 'CIRCUITPY' in d.mountpoint:
                    self.micro_drives.append(d.mountpoint)
        else:
            raise NotImplementedError
        Logger.info('Drives : {}'.format(self.micro_drives))
        self.root.ids['info_lbl'].text = str(len(self.micro_drives)) + ' microcontr\u00f4leur(s)\n' + str(len(self.root.ids['config_spnr'].values)) + ' configuration(s)'

    def set_config_type(self, txt):
        if txt != '-- Configuration --':
            self.config_type = txt
        
    def perform_config(self):
        if self.root.ids['config_spnr'].text == '-- Configuration --':
            p = PopupMessage()
            p.set_message('Configuration', 'Veuillez choisir la configuration des microcontr\u00f4leurs')
            p.open()
            return
        self.config_main()

    def config_main(self):
        try:
            for d in self.micro_drives:
                if os.name == 'nt':
                    f = open(d+'code.py','w')
                elif os.name == 'posix':
                    f = open(d+'/code.py','w')
                else:
                    raise NotImplementedError
                f.write(codepy_content.format(self.config_type))
                for c in self.configs:
                    f.write(config_content.format(c))
                f.flush()
                f.close()
                if os.name == 'nt':
                    subprocess.run('copy /Y .\\configs\\* {}'.format(d), shell=True, check = True)
                elif os.name == 'posix':
                    subprocess.run('cp -f ./configs/* {}'.format(d), shell=True, check = True)
                else:
                    raise NotImplementedError
                p = PopupMessage()
                p.set_message('Ecriture Ok', 'les {0} microcontr\u00f4leurs\nsont configur\u00e9es pour {1}'.format(len(self.micro_drives), self.config_type))
                p.open()
        except subprocess.CalledProcessError as e:
            Logger.warning ('subprocess copy : unable to copy ({0} : {1}'.format(e.cmd,e.output))
            p = PopupMessage()
            p.set_message('Erreur \u00e9criture', 'impossible d\'\u00e9crire la configuration')
            p.open()


if __name__ == '__main__':
    CpypcApp().run()