import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction
import time
from utilities import Notification

# ------------ parametres (pour le professeur) ----------
Rpont = 10000  # Ohm - résistance du pont
broche_entree = board.A0  # broche d'entree du potentiomètre
broche_alimentation = board.D2  # broche d'alimentation du montage
# -------------------------------------------------------

# ################## MODELE A MODIFIER PAR L'ELEVE ############################
def modele(R):
    temperature = R*0.006
    return temperature
# ############################################################################

# configuration de l'entrée analogique
entree_analogique = AnalogIn(broche_entree)
# configuration de l'alimentation du montage
alimentation = DigitalInOut(broche_alimentation)
alimentation.direction = Direction.OUTPUT
# config de la led interne
notif = Notification()

# boucle
while True:
    # alimenter le montage
    alimentation.value = True
    # attendre 50ms pour stabiliser le courant
    time.sleep(0.05)
    # calculer la tension à l'entrée analogique (16bits)
    tension = entree_analogique.value * 3.3 / 65535
    # arrêter d'alimenter le montage (lecture ok de l'entrée)
    alimentation.value = False
    # calculer la résistance de la thermistance
    r = Rpont * (3.3 / tension - 1)
    # calculer la température par le modèle
    temperature = modele(r)
    # afficher la température avec l'unité
    notif.notify(text='Uctn={:3.2f}V\nr={:3.2e}Ohms\nT={:3.0f}deg C')
    # attendre 2s
    time.sleep(2)
