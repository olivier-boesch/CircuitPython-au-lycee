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
broche_led_verte = board.D5
broche_led_jaune = board.D6
broche_led_rouge = board.D9
# -------------------------------------------------------

# ------------- setup
# configuration de la sortie de la led
led_verte = DigitalInOut(broche_led_verte)
led_verte.direction = Direction.OUTPUT  # c'est une sortie
led_jaune = DigitalInOut(broche_led_jaune)
led_jaune.direction = Direction.OUTPUT  # c'est une sortie
led_rouge = DigitalInOut(broche_led_rouge)
led_rouge.direction = Direction.OUTPUT  # c'est une sortie
# config des notifications
notif = Notification()
# show logo at startup
notif.oled_logo('media/logo_stex.bin')
time.sleep(2)

# -------------- boucle (loop)
while True:
    # feux vert
    led_verte.value = True
    led_jaune.value = False
    led_rouge.value = False
    notif.notify(text="Led Rouge")
    time.sleep(3)
    # feux orange
    led_verte.value = False
    led_jaune.value = False
    led_rouge.value = True
    notif.notify(text="Led Verte")
    time.sleep(1)
    # feux rouge
    led_verte.value = False
    led_jaune.value = True
    led_rouge.value = False
    notif.notify(text="Led Jaune")
    time.sleep(4)
