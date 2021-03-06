import board
from analogio import AnalogIn
import time
from utilities import Notification

# ------------ parametres (pour le professeur) ----------
broche_entree = board.A0  # broche d'entree du potentiomètre
# -------------------------------------------------------

# ############# PARAMETRE DU POTENTIOMETRE ###########
Rtot = 10000  # Ohm - résistance totale du potentiomètre


# ####################################################


# ################## MODELE A MODIFIER PAR L'ELEVE ###########################
def calcul_angle(r):
    ang = r * 1.0
    return ang


# ############################################################################


# configuration de l'entrée analogique
entree_analogique = AnalogIn(broche_entree)
# config des notifications
notif = Notification(print_data_tuple=True)
# show logo at startup
notif.oled_logo('saintex_logo.bin')
time.sleep(1)

# boucle
while True:
    # récupérer la valeur de l'entrée (16bits) calculer la tension à l'entrée analogique
    tension = entree_analogique.value * 3.3 / 65535
    # calculer la résistance du potentiomètre
    r = Rtot * (1.0 - tension / 3.3)
    # calculer l'angle par le modèle
    angle = calcul_angle(r)
    # afficher la mesure
    notif.notify(text='Ur={:3.2f}V\nr={:3.2e}Ohms\na={:3.0f}deg'.format(tension, r, angle))
    # attendre 200ms
    time.sleep(0.2)
