# -------------------------------------------------------
# Télémètre
#
# Olivier Boesch - Lycée Saint Exupéry
# Marseille
#
# -------------------------------------------------------

# ------------ imports
import board
from utilities import Notification, Button, SoundFile
from digitalio import DigitalInOut, Direction
import seeed_ultrasonicranger_v2
import time

# ------------ parametres ----------
broche_US = board.D4
broche_audio = board.A1
broche_activite = board.D13
# -------------------------------------------------------

# ------------- setup
# ecran oled ou port série pour l'affichage
notif = Notification()

# led d'activité
led = DigitalInOut(broche_activite)
led.direction = Direction.OUTPUT

# capteur ultrasons
capteur_us = seeed_ultrasonicranger_v2.UltrasonicRangerV2(broche_US)

# fichier son
audio = SoundFile("media/trop_pres.wav")

# afficher le logo mep au démarrage
notif.oled_logo('media/logo_mep.bin')
time.sleep(1)

# -------------- boucle (loop)
while True:
    # envoi du déclenchement de la mesure
    led.value = True  # on allume la led13 (rouge) pour indiquer le début la mesure
    # on fait la mesure (la duree est récupérée en ms)
    duree = capteur_us.measure_time_ms()
    # on éteint la led -> fin de mesure
    led.value = False
    # calcul de la distance en m
    distance = duree / 1000.0 * 342.0 / 2.0  # calcul de la distance en m
    # afffichage sur l'écran oled ou le port série
    if distance < 1:
        if not audio.playing():
            audio.play()
            time.sleep(distance / 2)
        texte = "attention !"
    else:
        texte = "ok"
    res = "-- {} --\nt = {:3.3f} ms \n d = {:3.2f} m".format(texte, duree, distance)
    notif.notify(res)
