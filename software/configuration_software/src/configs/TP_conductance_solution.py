# ----------------------------------------------------------------------
#
#   TP dosage par étalonnage par conductance
#
#   Idée : Jérôme Leboeuf (Lycée St Exupéry - Marseille)
#   Programme : Olivier Boesch (Lycée St Exupéry - Marseille)
#
#       (c) 2020
#
# ----------------------------------------------------------------------
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction
import time
from utilities import Notification

# ------------ parametres (pour le professeur) ----------
broche_entree = board.A0  # broche d'entree pour le conductimètre
broche_alimentation = board.D4  # broche d'alimentation
# -------------------------------------------------------

# ######### PARAMETRE DE LA RESISTANCE DE PONT #######
Rpont = 10000  # Ohm - résistance du pont


# ####################################################


# ################## MODELE A MODIFIER PAR L'ELEVE ###########################
def calcul_concentration(g):
    """paramètres :
        g : conductance de la solution en siemens (S)
       retourne :
        la valeur de la concentration de cette solurion"""
    C = 1.0 * r + 0.0
    return C


# ############################################################################

# ----- Setup

# configuration de l'entrée analogique
entree_analogique = AnalogIn(broche_entree)
# configuration de l'alimentation du montage
alimentation_montage = DigitalInOut(broche_alimentation)
alimentation_montage.direction = Direction.OUTPUT
# config des notifications
notif = Notification()
# show logo at startup
notif.oled_logo('mep_logo.bin')
time.sleep(1)

# ----- Boucle
while True:
    # Alimenter le montage
    alimentation_montage.value = True
    # attendre la stabilisation (0.1s)
    time.sleep(0.1)
    # récupérer la valeur de l'entrée (16bits) et calculer la tension à l'entrée analogique
    tension = entree_analogique.value * 3.3 / 65535
    # Arrêter d'alimenter le montage
    alimentation_montage.value = False
    # calculer la résistance de la solution
    if tension < 0.0005:
        r = float('inf')
    else:
        r = Rpont * (3.3 / tension - 1.0)
    # calculer la conductance
    if r < 0.0005:
        g = float('inf')
    else:
        g = 1 / r
    # calculer la concentration par le modèle C=f(g)
    concentration = calcul_concentration(g)
    # afficher la mesure
    notif.notify(text='Ur={:3.2f}V\nr={:3.2e}Ohms\nC={:3.0f}mol/L'.format(tension, r, concentration))
    # attendre 0.5s
    time.sleep(0.5)
