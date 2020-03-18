import serial
import time
from serial.tools import list_ports
import os
import requests
import requests.exceptions
from collections import OrderedDict

circuitpython_releases_url = "https://api.github.com/repos/adafruit/circuitpython/releases"
circuitpython_libraries_releases_url = ""

# file utilities for windows or linux
if os.name == 'nt':
    import win32api
elif os.name == 'posix':
    import psutil
else:
    raise NotImplementedError
    
def get_firmware_releases(board, lang='en',  include_alpha=False, include_beta=False, include_rc=False):
    """get_firmware_releases: gets all releases for a board and language
        returns an ordered dict with versions as keys and download links"""
    try:
        # get data as json
        req = requests.get(circuitpython_releases_url)
        data = req.json()
        releases = OrderedDict()
        # walk through releases
        for r in data:
            release_links = []
            release_name = r['tag_name']
            release_link = None
            
            # walk through assets to find links
            for a in r['assets']:
                # store if it's the right board
                if board in a['name']:
                    release_links.append(a['browser_download_url'])
                    
            # if several links
            if len(release_links) > 1:
                # walk through links to find the right language
                for link in release_links:
                    if (board + '-' + lang) in link:
                        release_link = link
                        break
            # only one: store it
            elif len(release_links) == 1:
                release_link = release_links[0]
            # no link: go to next release
            else:
                continue
                
            # store only if condition is ok
            condition = True
            if not include_alpha:
                condition = condition and 'alpha' not in release_name
            if not include_beta:
                condition = condition and 'beta' not in release_name
            if not include_rc:
                condition = condition and 'rc' not in release_name
            if condition:
                releases[release_name] = release_link
        # return releases with links
        return releases
    except requests.exceptions.ConnectionError as e :
        return None

def update_drives(drive_name_pattern):
        """search for µC drives 'CIRCUITPY' or 'FEATHERBOOT' for firmware"""
        # search for drives
        micro_drives = []
        # search for windows
        if os.name == 'nt':
            drives = win32api.GetLogicalDriveStrings().split('\x00')[:-1]
            for d in drives:
                try:
                    volume_info = win32api.GetVolumeInformation(d)
                    if drive_name_pattern in volume_info[0]:
                        micro_drives.append(d)
                except win32api.error as e :
                    Logger.warning('Win32api Error {0} : ({1}) {2} for drive {3}'.format(e.winerror, e.funcname, e.strerror,d))
        # search for linux and possibly macos
        elif os.name == 'posix':
            disk_info = psutil.disk_partitions()
            for d in disk_info:
                if drive_name_pattern in d.mountpoint:
                    micro_drives.append(d.mountpoint)
        else:
            raise NotImplementedError
        # return results
        return micro_drives
        
def eject_drive(drive):
    # for windows : for eject drive to flush write buffer
    if os.name == 'nt':
        remove_drive_app = os.path.join('tools', 'RemoveDrive.exe')
        subprocess.run(remove_drive_app + " " + d + " -e", shell=True)
    # for linux : unmount drives
    elif os.name == 'posix':
        subprocess.run('umount' + " " + d, shell=True)
        
        
def update_ports_list(port_description_pattern):
    """get available serial ports for feather
    port_description_pattern: use "CircuitPython" or "Arduino" """
    # get an iterator with available serial ports
    comportslist = list_ports.comports()
    # set list for com ports with M4 connected
    ports = [item.device for item in comportslist if port_description_pattern in item.description]
    # return result
    return ports

class CircuitPythonBoard:
    def __init__(self, device=None):
        self._device = device
        self._serial_connection = None
        if self._device is not None:
            self.connect()
        
    def set_device(self, device):
        self._device = device
        
    def connect(self):
        self._serial_connection = serial.Serial(self._device, 115200)
    
    def disconnect(self):
        if self._serial_connection is not None:
            self._serial_connection.close()
            self._serial_connection = None
            
    def is_connected(self):
        return self._serial_connection is not None
        
    def _send_command(self, cmd, raw = False):
        if self._serial_connection is not None:
            if not raw:
                cmd += "\r\n"
                self._serial_connection.write(cmd.encode())
            else:
                self._serial_connection.write(cmd)
    def switch_to_repl(self):
        self._send_command(b'\x03\n', True)
        time.sleep(0.1)  # leave enough time to switch to REPL  
        
    def switch_to_run(self):
        self._send_command(b'\x04', True)
            
    def reset_to_normal(self):
        self.switch_to_repl()
        self._send_command('import microcontroller')
        self._send_command('microcontroller.reset()')
        self.disconnect()
        
    def reset_to_bootloader(self):
        self.switch_to_repl()
        self._send_command('import microcontroller')
        self._send_command('microcontroller.on_next_reset(microcontroller.RunMode.BOOTLOADER)')
        self._send_command('microcontroller.reset()')
        self.disconnect()
        
    def format_storage(self):
        self.switch_to_repl()
        self._send_command('import storage')
        self._send_command('storage.erase_filesystem()')
        self.disconnect()
    
