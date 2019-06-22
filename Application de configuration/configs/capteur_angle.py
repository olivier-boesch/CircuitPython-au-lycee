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
def modele(R):
    angle = R*0.1
    return angle
# ############################################################################


# configuration de l'entrée analogique
entree_analogique = AnalogIn(broche_entree)
# config des notifications
notif = Notification()

# boucle
while True:

    # récupérer la valeur de l'entrée (16bits) calculer la tension à l'entrée analogique
    tension = entree_analogique.value * 3.3 / 65535
    print('tension: {:5.3f} V'.format(tension), end='; ')
    # calculer la résistance du potentiomètre
    r = Rtot*(1.0-tension/3.3)
    # calculer l'angle par le modèle
    angle = modele(r)
    # afficher la mesure
    notif.notify(text='Ur={:3.2f}V\nr={:3.2e}Ohms\na={:3.0f}deg')
    # attendre 1s
    time.sleep(1)

