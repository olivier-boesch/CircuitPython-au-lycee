from serial import Serial, EIGHTBITS, STOPBITS_ONE, PARITY_NONE
from serial.tools.list_ports import comports

from kivy.app import App
from kivy.clock import Clock
from kivy.logger import Logger


def list_available_feathers():
    """list_available_feathers : list available feathers MCU in com ports
                                 and return a list of tuples with device and description"""
    return [(port.device, port.description) for port in comports() if 'Feather' in port.description]


class DatacapApp(App):
    """Main Application class"""
    def __init__(self):
        super().__init__()
        self.serial_ports = None

    def build(self):
        super().build()
        Clock.schedule_interval(lambda dt: self.update_ports_spinner(), 1)

    def change_serial_port(self, val):
        print(val)

    def update_ports_spinner(self):
        self.serial_ports = {port[0]:port[1] for port in list_available_feathers()}
        Logger.info("Serial: Updating ports ({:s}".format(str(self.serial_ports)))
        keys = list(self.serial_ports.keys())
        self.root.ids['port_spnnr'].values = tuple(keys)
        if self.root.ids['port_spnnr'].text not in keys:
            if len(self.serial_ports.keys()) == 1:
                self.root.ids['port_spnnr'].text = keys[0]
            elif len(self.serial_ports.keys()) == 0:
                self.root.ids['port_spnnr'].text = 'Rien n\'est détecte'
            else:
                self.root.ids['port_spnnr'].text = '{:3d} ports trouves'.format(len(keys))


    def open_port(self, port):
        pass

app = DatacapApp()
app.run()