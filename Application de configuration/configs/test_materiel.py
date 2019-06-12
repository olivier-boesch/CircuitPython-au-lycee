# --------------------------------------------------------------------------
# test_materiel :
# test du microcontrolleur et des connexions
#
# --------------------------------------------------------------------------

import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction
import time
from utilities import Notification, GREEN, CYAN, YELLOW, PURPLE

notif = Notification(always_serial_output=True)

while True:
    # test écran
    notif.notify(color=PURPLE, text="test ecran")
    time.sleep(1)
    notif.show_logo_bin()
    time.sleep(1)
    notif.notify(color=PURPLE, text='progress bar running')
    time.sleep(2)

    for i in range(0, 101, 10):
        notif.oled_bar(i)
    time.sleep(2)

    # test entrees analogiques
    analog_ins = []
    analog_ins.append(AnalogIn(board.A0))
    analog_ins.append(AnalogIn(board.A1))
    analog_ins.append(AnalogIn(board.A2))
    analog_ins.append(AnalogIn(board.A3))
    analog_ins.append(AnalogIn(board.A4))
    analog_ins.append(AnalogIn(board.A5))

    i=0
    for input in analog_ins:
        val = input.value
        u = val * 3.3 / 65535
        ok = u > 3.0 ? True : False
        notif.notify(color=CYAN, text='analog in A{:d}: u={:3.2f}, val={:d}, ok: {}'.format(i, u, val, str(ok)))
        i += 1

    # test entrees digitales
    digital_ins.append(DigitalInOut(board.D4))
    digital_ins.append(DigitalInOut(board.D5))
    digital_ins.append(DigitalInOut(board.D6))
    digital_ins.append(DigitalInOut(board.D9))
    digital_ins.append(DigitalInOut(board.D10))
    digital_ins.append(DigitalInOut(board.D11))
    digital_ins.append(DigitalInOut(board.D12))
    for din in digital_ins:
        din.direction = Direction.INPUT
        if din.value:
            notif.notify(color=YELLOW, text='digital in: u={:3.2f}, val={:d}, ok: {}'.format(i, u, val, str(ok)))
