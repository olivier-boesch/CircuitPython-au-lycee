#!/usr/bin/python3
import hardware_ops

from kivy.app import App
from kivy.logger import Logger
from kivy.clock import Clock
from kivy.uix.popup import Popup

class ConfirmPopup(Popup):
    pass
    
    
class InfoPopup(Popup):
    def set_info(self, txt):
        self.ids['info_lbl'].text = txt
        

class CirPySupportApp(App):
    popup = None
    ports = []
    def build(self):
        #update ports list and drive list every 1s
        self.update_ports_list_event = Clock.schedule_interval(lambda dt: self.update_ports(), 1.)

    def format_storage(self):
        if self.popup is not None:
            self.popup.dismiss()
        self.update_ports_list_event.cancel()
        mcu = hardware_ops.CircuitPythonBoard(self.ports[0])
        mcu.format_storage()
        del mcu
        self.update_ports_list_event = Clock.schedule_interval(lambda dt: self.update_ports(), 1.)
        p = InfoPopup()
        p.open()
        p.set_info('Procédure terminée\nMerci d\'éjecter le disque à présent.')
            
    def open_confirm(self):
        if len(self.ports) == 1:
            self.popup = ConfirmPopup()
            self.popup.open()
        elif len(self.ports) == 0:
            p = InfoPopup()
            p.open()
            p.set_info('pas de microcontrolleur connecté')   
        else:
            p = InfoPopup()
            p.open()
            p.set_info('veuillez connecter un seul microcontroleur à la fois')

    def update_ports(self):
        self.ports = hardware_ops.update_ports_list(port_description_pattern="Feather")
        Logger.info("ports found: {}".format(str(self.ports)))
        self.root.ids['mcu_lbl'].text = "{} microcontrolleurs détectés".format(len(self.ports))


app = CirPySupportApp()
app.run()
