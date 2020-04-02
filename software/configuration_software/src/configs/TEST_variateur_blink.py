# -------------------------------------------------------
# Variateur avec consigne
#
# Olivier Boesch - Lycée Saint Exupéry
# Marseille
#
# -------------------------------------------------------

# ------------ imports
import board
import time
from utilities import Notification
import pulseio
import analogio

# ------------ parametres ----------
broche_led = board.D9
# -------------------------------------------------------

# ------------- setup
# configuration de la sortie de la led en PWM
led = pulseio.PWMOut(broche_led, frequency=1, duty_cycle=2 ** 15, variable_frequency=True)
# configuration de l'entrée du potentiomètre
pot = analogio.AnalogIn(board.A0)
# config des notifications
notif = Notification()
# show logo at startup
notif.oled_logo('media/logo_stex.bin')
time.sleep(2)

# -------------- boucle (loop)
while True:
    # set duty cycle of led with pot value
    led.frequency = int(pot.value / 5000.0) + 1
    # draw a beautiful bar ;-)
    notif.oled_bar(pot.value / 65535 * 100)
