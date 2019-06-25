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
from utilities import Notification, GREEN, CYAN, YELLOW, PURPLE, Button

# init ====================================
notif = Notification(always_serial_output=True)
fm_str = "A0|A1|A2|A3|A4|A5\n {:1.0f}| {:1.0f}| {:1.0f}| {:1.0f}| {:1.0f}| {:1.0f} \nD|4{:s}|10{:s}|11{:s}|12{:s}|{:s}{:s}{:s}"


#Programme principal ======================
# test écran ------------------------------
notif.notify(color=PURPLE, text="test matériel")
time.sleep(1)
# test logo -------------------------------
notif.oled_logo('saintex_logo.bin')
time.sleep(2)
# test progress bar -----------------------
notif.notify(color=CYAN, text='progress bar running')
time.sleep(2)
for i in range(0, 101, 10):
    notif.oled_bar(i)
time.sleep(2)

# test entrées ----------------------------
analog_ins = list()
analog_ins.append(AnalogIn(board.A0))
analog_ins.append(AnalogIn(board.A1))
analog_ins.append(AnalogIn(board.A2))
analog_ins.append(AnalogIn(board.A3))
analog_ins.append(AnalogIn(board.A4))
analog_ins.append(AnalogIn(board.A5))

digital_ins = list()
digital_ins.append(DigitalInOut(board.D4))
digital_ins.append(DigitalInOut(board.D10))
digital_ins.append(DigitalInOut(board.D11))
digital_ins.append(DigitalInOut(board.D12))
for inp in digital_ins:
    inp.direction = Direction.INPUT

A = Button(board.D9, True)
B = Button(board.D6, True)
C = Button(board.D5, True)

din_values = [False for i in range(4)]
ain_values = [0.0 for i in range(6)]

# Led interne #13
internal_led = DigitalInOut(board.D13)
internal_led.direction = Direction.OUTPUT
internal_led.value = True

# Boucle ===============================
# test es sur écran ou série
notif.notify(color=YELLOW, text='TEST ES...')
time.sleep(2)
while True:
    i=0
    for input in analog_ins:
        val = input.value
        u = val * 3.3 / 65535
        ain_values[i] = u
        i += 1

    i=0
    for din in digital_ins:
        din_values[i] = "T" if din.value else "F"
        i += 1

    A.check()
    B.check()
    C.check()

    val_buttons = []
    val_buttons.append("A" if A.is_pushed() else " ")
    val_buttons.append("B" if B.is_pushed() else " ")
    val_buttons.append("C" if C.is_pushed() else " ")
    notif.notify(color=YELLOW,text=fm_str.format(*(ain_values+din_values+val_buttons)))
    internal_led.value = not internal_led.value
    if not notif.oled_display:
        time.sleep(0.2)