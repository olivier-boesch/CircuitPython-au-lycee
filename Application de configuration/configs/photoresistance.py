import board
from analogio import AnalogIn
import time
from utilities import Notification

# ------------ parametres (pour le professeur) ----------
Rpont = 10000  # Ohm - résistance du pont
broche_entree = board.A0  # broche d'entree du potentiomètre
# -------------------------------------------------------

# ################## MODELE A MODIFIER PAR L'ELEVE ############################
def modele(R):
    luminosite = R*0.006
    return luminosite
# ############################################################################

# configuration de l'entrée analogique
entree_analogique = AnalogIn(broche_entree)
# config des notifications
notif = Notification()

# boucle
while True:
    # calculer la tension à l'entrée analogique
    tension = entree_analogique.value * 3.3 / 65535
    # calculer la résistance de la photorésistance
    r = Rpont * (3.3 / tension - 1)
    # calculer la luminosité par le modèle
    luminosite = modele(r)
    # afficher les valeurs (lcd ou serie)
    notif.notify(text='Uldr={:3.2f}V\nr={:3.2e}Ohms\nl={:3.0f}lux')
    # attendre 1s
    time.sleep(1)