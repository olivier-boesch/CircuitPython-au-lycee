# -------------------------------
#
# capteur d'angle
#
# Olivier Boesch - Lycée Saint Exupéry
# Marseille
#
# -------------------------------

# ************* SCHEMA ***************
#  GND----Rpont-------potentiomètre-----3,3V
#                 |
#                 A0
# ************************************

import board
from analogio import AnalogIn
import time
from utilities import Notification

# ------------ parametres ----------
broche_entree = board.A0  # broche d'entree du potentiomètre
# -------------------------------------------------------

# ############# PARAMETRE DU POTENTIOMETRE ###########
Rtot = 10000.0  # Ohm - résistance totale du potentiomètre
Rpont = 10000.0 # Ohm - valeur de la résistance de pont
# ####################################################


# configuration de l'entrée analogique
entree_analogique = AnalogIn(broche_entree)
# config des notifications
notif = Notification(always_serial_output=True)
# show logo at startup
notif.oled_logo('saintex_logo.bin')
time.sleep(1)

# boucle
while True:

    # récupérer la valeur de l'entrée (16bits) calculer la tension à l'entrée analogique
    tension = entree_analogique.value * 3.3 / 65535.0
    # calculer la résistance du potentiomètre
    r_pot = (3.30 / tension - 1.0) * Rpont
    # calculer l'angle par le modèle
    angle = r_pot * 300.0 / Rtot
    # afficher la mesure
    notif.notify(text='Ur={:3.2f} V\nr={:3.2f} Ohms\na={:3.0f} deg'.format(tension, r_pot, angle))