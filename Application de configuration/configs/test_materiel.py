# --------------------------------------------------------------------------
# test_materiel :
# test du microcontroleur et des connexions
# v1-2019 : olivier boesch
# --------------------------------------------------------------------------
# imports =================================
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction
import time
from utilities import Notification, GREEN, CYAN, YELLOW, PURPLE

# init ====================================
notif = Notification(always_serial_output=True)
fm_str = "A0A1A2A3A4A5A6\n"+ "{:2.1f}" * 6 + '\n' + '{:1d}' * 7


#Programme principal ======================
# test écran ------------------------------
notif.notify(color=PURPLE, text="test ecran")
time.sleep(1)
# test logo -------------------------------
notif.show_logo_bin()
time.sleep(1)
# test progress bar -----------------------
notif.notify(color=CYAN, text='progress bar running')
time.sleep(2)
for i in range(0, 101, 10):
    notif.oled_bar(i)
time.sleep(2)

# test entrées ----------------------------
analog_ins = []
analog_ins.append(AnalogIn(board.A0))
analog_ins.append(AnalogIn(board.A1))
analog_ins.append(AnalogIn(board.A2))
analog_ins.append(AnalogIn(board.A3))
analog_ins.append(AnalogIn(board.A4))
analog_ins.append(AnalogIn(board.A5))

digital_ins = []
digital_ins.append(DigitalInOut(board.D4))
digital_ins.append(DigitalInOut(board.D5))
digital_ins.append(DigitalInOut(board.D6))
digital_ins.append(DigitalInOut(board.D9))
digital_ins.append(DigitalInOut(board.D10))
digital_ins.append(DigitalInOut(board.D11))
digital_ins.append(DigitalInOut(board.D12))
for inp in digital_ins:
    inp.direction = Direction.INPUT

din_values = [False for i in range(7)]
ain_values = [0.0 for i in range(6)]
# Boucle ===============================
# test es sur écran ou série
while True:
    i=0
    for input in analog_ins:
        val = input.value
        u = val * 3.3 / 65535
        ain_values[i] = u
        i += 1

    i=0
    for din in digital_ins:
        din_values[i] = din.value
        i += 1
    notif.notify(color=YELLOW,fm_str.format(*ain_values,*din_values))
