# -------------------------------------------------------
#
#
#
#
#
# -------------------------------------------------------

# ------------ imports
import board
import time
from utilities import Notification
from digitalio import DigitalInOut, Direction

# ------------ parametres ----------
broche_led = board.D4
# -------------------------------------------------------

# ------------- setup
# configuration de la sortie de la led
led = DigitalInOut(broche_led)
led.direction = Direction.OUTPUT  # c'est une sortie
# config des notifications
notif = Notification()
# show logo at startup
notif.oled_logo('media/logo_stex.bin')
time.sleep(2)

# -------------- boucle (loop)
while True:
    led.value = True
    notif.notify(text="Led allumee")
    time.sleep(1)
    led.value = False
    notif.notify(text="Led eteinte")
    time.sleep(1)