#!/usr/bin/env python3
"""

 CirPyConfig : Application de configuration
       pour microcontroleur M4 express Adafruit

   Olivier Boesch (c) 2019
   LICENSE : MIT

"""
import os
import os.path
import distutils.dir_util
import time
import subprocess
# ------------ now useless with PyInstaller and --noconsole option
# for windows : don't write on console -> leads to an error with pythonw.exe
# if os.name == 'nt':
#     os.environ["KIVY_NO_CONSOLELOG"] = "1"
# -----------------------------------------
# kivy config import
from kivy.config import Config
# it's a desktop app
Config.set('kivy', 'desktop', 1)
# start with window maximized
Config.set('graphics', 'window_state', 'maximized')
# disable multitouch -> otherwise it draws an orange circle on others click than left one
Config.set('input', 'mouse', 'mouse,disable_multitouch')
# kivy components import
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.logger import Logger

# file utilities for windows or linux
if os.name == 'nt':
    import win32api
elif os.name == 'posix':
    import psutil
else:
    raise NotImplementedError

# minimum content of code.py
codepy_content = """
# choix de la configuration executee
config = '{}'

"""

# content of code py for each config
config_content = """
if config == \'{0}\':
    import {0}

"""


# ------- Popup for message
class PopupMessage(Popup):
    """PopupMessage : display a message box"""
    def set_message(self, title, text):
        """set_message: set title and text"""
        self.title = title
        self.ids['message_content_lbl'].text = text

    def close_after(self, dt=2.):
        """close popup automatically after a short time (us 2s)"""
        Clock.schedule_once(lambda t: self.dismiss(), dt)


# ------- Popup for operation (message centered)
class PopupOperation(Popup):
    """PopupOperation : display a centered non dismissible message box"""
    def set_message(self, title, text):
        """set_message: set title and text"""
        self.title = title
        self.ids['message_content_lbl'].text = text

    def close_after(self, dt=2.):
        """close popup automatically after a short time (us 2s)"""
        Clock.schedule_once(lambda t: self.dismiss(), dt)


class CpycApp(App):
    """ Main application class"""
    def __init__(self):
        super().__init__()
        self.drive_update = None
        self.configs = None
        self.micro_drives = None
        self.config_type = None
        self.progress_window = None

    def build(self):
        """app graphical startup"""
        #set app window name
        self.title = 'CirPyConfig'
        # schedule drives update at 1s interval
        self.drive_update = Clock.schedule_interval(lambda dt: self.update_drives(), 1.0)
        # schedule config at startup (0.2s)
        Clock.schedule_once(lambda dt: self.update_config(), 0.2)

    def update_label_infos(self):
        """updates the info label with number of configs and µCs"""
        s = ''
        if self.configs is not None:
            s += str(len(self.configs)) + " Configuration(s); "
        if self.micro_drives is not None:
            s += str(len(self.micro_drives)) + " Microcontr\u00f4leur(s); "
        self.root.ids['info_lbl'].text = s[:-2]

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
            b.font_name = 'Oxanium-Light.ttf'
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
                    Logger.warning('Win32api Error {0} : ({1}) {2} for drive {3}'.format(e.winerror,
                                                                                         e.funcname,
                                                                                         e.strerror,d))
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
            self.root.ids['choosen_config_lbl'].text = "Pas de configuration choisie"

    def perform_config(self):
        """verify conditions and call config_main if ok"""
        # can't go if no config is selected
        if self.config_type is None:
            p = PopupMessage()
            p.set_message("Erreur de configuration", "Veuillez choisir une configuration")
            p.open()
            p.close_after()
        # it is useless to go if there's no µC
        elif self.micro_drives is None or len(self.micro_drives) == 0:
            p = PopupMessage()
            p.set_message("Erreur de configuration", "Veuillez brancher au moins un microcontr\u00f4leur")
            p.open()
            p.close_after()
        else:
            # open operation window
            self.progress_window = PopupOperation()
            self.progress_window.set_message("Configuration en cours", "Veuillez patienter...")
            self.progress_window.open()
            # launch config operation for next gui next frame
            Clock.schedule_once(lambda dt: self.config_main(), 0)

    def config_main(self):
        """main function to apply config (does the real thing)"""
        try:
            # disable drives updates
            self.drive_update.cancel()
            # iterate over drives
            for d in self.micro_drives:
                # copy configs dir on µC drive
                src = os.path.abspath(os.path.join('.', 'configs'))
                Logger.info("Copy files: from " + src + " to " + d)
                ret = distutils.dir_util.copy_tree(src, d, preserve_mode=0, preserve_times=0,
                                                   preserve_symlinks=0, update=0, verbose=0, dry_run=0)
                Logger.info("Copy files: done ->" + str(ret))
                # wait a little
                time.sleep(0.1)
                # open code.py file
                f = open(os.path.join(d, 'code.py'), 'w')
                # write code.py file
                f.write(codepy_content.format(self.config_type))  # write choosen config
                for c in self.configs:
                    f.write(config_content.format(c))  # write access to all configs
                f.flush()  # ensure file is written
                f.close()
                # for windows : for eject drive to flush write buffer
                if os.name == 'nt':
                    remove_drive_app = os.path.join('tools', 'RemoveDrive.exe')
                    subprocess.run(remove_drive_app + " " + d + " -e", shell=True)
                    Logger.info("Copy files: drive " + str(d) + "ejected")
                # for linux : unmount drives
                elif os.name == 'posix':
                    subprocess.run('umount' + " " + d, shell=True)
                    Logger.info("Copy files: drive " + str(d) + "unmounted")
            # tell everything's gone right
            # TODO: how to verify
            p = PopupMessage()
            p.set_message('Ecriture Ok !', '{0} microcontr\u00f4leur(s)\nconfigur\u00e9(s) pour {1}'.format(
                len(self.micro_drives),
                self.config_type)
                          )
            p.open()
        # react when copy is not possible
        except subprocess.CalledProcessError as e:
            Logger.error('subprocess copy : unable to copy ({0} : {1}'.format(e.cmd,e.output))
            p = PopupMessage()
            p.set_message('Erreur \u00e9criture', 'impossible d\'\u00e9crire la configuration')
            p.open()
            p.close_after()
        finally:
            # reschedule drives updates
            self.drive_update()
            # close operation window (and destroy it)
            self.progress_window.dismiss()
            del self.progress_window
            self.progress_window = None


if __name__ == '__main__':
    CpycApp().run()
