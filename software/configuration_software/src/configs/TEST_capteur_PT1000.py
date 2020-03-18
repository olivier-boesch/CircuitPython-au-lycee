# -------------------------------
#
# capteur PT1000 - TEST
#
# Olivier Boesch - Lycée Saint Exupéry
# Marseille
#
# -------------------------------

import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction
import time
from utilities import Notification, RED, GREEN

# ************* SCHEMA ***************
#  GND----Rpont-------PT1000-----D4
#                 |
#                 A0
# ************************************

# ------------ parametres ----------
broche_entree = board.A0  # broche d'entree du potentiomètre
broche_alimentation = board.D4 # broche pour alimentation du montage
# -------------------------------------------------------

# ############# PARAMETRE DU POTENTIOMETRE ###########
Rpont = 1000.0 # Ohm - valeur de la résistance de pont
# ####################################################

# ------------- setup
# configuration de l'entrée analogique
entree_analogique = AnalogIn(broche_entree)
# alimentation
alimentation = DigitalInOut(broche_alimentation)
alimentation.direction = Direction.OUTPUT
# config des notifications
notif = Notification(always_serial_output=True, always_led_on=True)
# logo mep
notif.intro()

# -------------- boucle
while True:
    # allumer la led en rouge pour indiquer la mesure
    notif.led(RED)
    # alimenter le montage
    alimentation.value = True
    # attendre la stabilisation des valeurs (0.2s)
    time.sleep(0.2)
    # récupérer la valeur de l'entrée (16bits=65536) calculer la tension à l'entrée analogique
    tension = entree_analogique.value * 3.3 / 65535
    # arrêter l'alimentation
    alimentation.value = False
    # allumer la led en vert pour indiquer la fin de mesure
    notif.led(GREEN)
    # calculer la résistance de la PT1000
    r_pt1000 = (3.30 / tension - 1.0) * Rpont
    # calculer la temperature par le modèle
    temperature = r_pt1000 * 0.25 - 259.25
    # afficher la mesure (avec la led en vert)
    notif.notify(color=GREEN, text='Ur={:3.4f} V\nr={:3.0f} Ohms\ntemp={:3.0f} oC'.format(tension, r_pt1000, temperature))
    # attendre pour eviter l'auto-échauffement de la résistance (2s)
    time.sleep(2)