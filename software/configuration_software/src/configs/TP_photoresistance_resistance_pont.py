import board
from analogio import AnalogIn
import time
from utilities import Notification

# ------------ parametres (pour le professeur) ----------
broche_entree = board.A0  # broche d'entree du potentiomètre


# -------------------------------------------------------


# ################## MODELES A MODIFIER PAR L'ELEVE ############################
# calcul de la resistance
def calcul_resistance(u):
    r = u * 1.0
    return r


# calcul de la luminosité
def calcul_luminosite(R):
    lum = R * 1.0
    return lum


# ############################################################################


# configuration de l'entrée analogique
entree_analogique = AnalogIn(broche_entree)
# config des notifications
notif = Notification()
# show logo at startup
notif.oled_logo('saintex_logo.bin')
time.sleep(1)

# boucle
while True:
    # calculer la tension à l'entrée analogique
    tension = entree_analogique.value * 3.3 / 65535
    # calculer la résistance de la photorésistance
    r = calcul_resistance(tension)
    # calculer la luminosité par le modèle
    luminosite = calcul_luminosite(r)
    # afficher les valeurs (lcd ou serie)
    notif.notify(text='Uldr={:3.2f}V\nr={:3.2e}Ohms\nl={:3.0f}lux'.format(tension, r, luminosite))
    # attendre 1s
    time.sleep(1)
