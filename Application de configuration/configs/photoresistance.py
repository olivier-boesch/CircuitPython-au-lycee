import board
from analogio import AnalogIn
import time
import adafruit_dotstar as dotstar

# ------------ parametres (pour le professeur) ----------
Rpont = 10000  # Ohm - résistance du pont
broche_entree = board.D0  # broche d'entree du potentiomètre
# -------------------------------------------------------

# ################## MODELE A MODIFIER PAR L'ELEVE ############################
def modele(R):
    luminosite = R*0.006
    return luminosite
# ############################################################################

# configuration de l'entrée analogique
entree_analogique = AnalogIn(broche_entree)
# config de la led interne
led = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.3)

# boucle
while True:
    # Flasher la led en vert pour montrer l'instant de la mesure
    led[0] = (0, 255, 0)
    time.sleep(0.05)
    # calculer la tension à l'entrée analogique
    tension = entree_analogique.value * 3.3 / 65535
    print('tension: {:5.3f} V'.format(tension), end='; ')
    # calculer la résistance du potentiomètre
    r = Rpont * (3.3 / tension - 1)
    print('valeur resistance: {:6d} Ohms'.format(int(r)), end='; ')
    # calculer l'angle par le modèle
    luminosite = modele(r)
    # afficher l'angle avec l'unité
    print('luminosite: {:5d} lx'.format(int(luminosite)))
    # allumer la led en cyan (attente)
    led[0] = (0, 150, 255)
    # attendre 1s
    time.sleep(1)