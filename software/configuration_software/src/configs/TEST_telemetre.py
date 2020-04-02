# -------------------------------------------------------
# Pressiomètre
# Olivier Boesch - Lycée Saint Exupéry
# Marseille
#
# -------------------------------------------------------

# ------------ imports
import board
from utilities import Notification, Button
import pulseio
from digitalio import DigitalInOut, Direction
import seeed_ultrasonicranger_v2
import time

# ------------ parametres ----------
broche_US = board.D4
broche_ButC = board.D5
broche_activite = board.D13
# -------------------------------------------------------

# ------------- setup
# ecran oled ou port série pour l'affichage
notif = Notification()
# bouton pour déclencher la mesure
butC = Button(broche_ButC, reverse=True)

# led d'activité
led = DigitalInOut(broche_activite)
led.direction = Direction.OUTPUT

# capteur ultrasons
capteur_us = seeed_ultrasonicranger_v2.UltrasonicRangerV2(broche_US)

# afficher le logo mep au démarrage
notif.oled_logo('media/logo_mep.bin')
time.sleep(1)

# inviter l'utilisateur à appuyer sur le bouton C
notif.notify("Veuillez appuyer\nsur le bouton C\npour faire une mesure")

# -------------- boucle (loop)
while True:
    # attente d'un appui sur le bouton C pour déclencher la mesure
    butC.check()
    while not butC.is_pushed():
        butC.check()

    # envoi du déclenchement de la mesure
    led.value = True  # on allume la led13 (rouge) pour indiquer le début la mesure
    # on fait la mesure (la duree est récupérée en ms)
    duree = capteur_us.measure_time_ms()
    # on éteint la led -> fin de mesure
    led.value = False
    # calcul de la distance en m
    distance = duree / 1000.0 * 342.0 / 2.0  # calcul de la distance en m
    # afffichage sur l'écran oled ou le port série
    res = "----- telemetre -----\nt = {:3.3f} ms \n d = {:3.2f} m".format(duree, distance)
    notif.notify(res)
