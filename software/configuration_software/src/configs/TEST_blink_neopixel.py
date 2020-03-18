# -------------------------------------------------------
#  
# Test de la neopixel
#
#  Olivier Boesch (c) 2019
#
# -------------------------------------------------------

# ------------ imports
import board
import time
import neopixel
from utilities import Notification, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, ORANGE, OFF
# ------------ parametres ----------
# -------------------------------------------------------

# ------------- setup
# configuration de la led neopixel
notif = Notification(always_led_on=True, led_brightness=0.7)

# -------------- boucle (loop)
while True:
    notif.notify("Rouge", RED)
    time.sleep(0.5)
    notif.notify("Jeune", YELLOW)
    time.sleep(0.5)
    notif.notify("Vert", GREEN)
    time.sleep(0.5)
    notif.notify("Cyan", CYAN)
    time.sleep(0.5)
    notif.notify("Bleu", BLUE)
    time.sleep(0.5)
    notif.notify("Magenta", PURPLE)
    time.sleep(0.5)
    notif.notify("Orange", ORANGE)
    time.sleep(0.5)
    notif.notify("Eteint", OFF)
    time.sleep(0.5)
