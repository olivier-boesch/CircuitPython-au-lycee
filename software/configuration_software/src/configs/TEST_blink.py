# -------------------------------------------------------
#
# BLINK TEST pour Platine Circuitpython au lycée
#
#  Olivier Boesch (c) 2019
#   V2 : ajout de la led neopixel dans le test
#
# -------------------------------------------------------

# ------------ imports
import board
import time
from utilities import Notification, GREEN, OFF
from digitalio import DigitalInOut, Direction

# ------------ parametres ----------
broche_led = board.D13  # led rouge sur le côté de la carte
# -------------------------------------------------------

# ------------- setup
# configuration de la sortie de la led
led = DigitalInOut(broche_led)
led.direction = Direction.OUTPUT  # c'est une sortie !
# config des notifications
notif = Notification(always_led_on=True, always_serial_output=True, led_brightness=0.5)
# show logo at startup
notif.oled_logo('media/logo_mep.bin')
time.sleep(2)

# -------------- boucle (loop)
while True:
    led.value = True
    notif.notify(text="Leds allumees", color=GREEN)
    time.sleep(1)
    led.value = False
    notif.notify(text="Leds eteintes", color=OFF)
    time.sleep(1)
