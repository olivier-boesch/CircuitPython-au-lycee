import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction
import time
import adafruit_dotstar as dotstar

# ------------ parametres (pour le professeur) ----------
Rpont = 10000  # Ohm - résistance du pont
broche_entree = board.D0  # broche d'entree du potentiomètre
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
led = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.3)

# boucle
while True:
    # Flasher la led en vert pour montrer l'instant de la mesure
    led[0] = (0, 255, 0)
    time.sleep(0.05)
    # alimenter le montage
    alimentation.value = True
    # attendre pour stabiliser le courant
    time.sleep(0.05)
    # calculer la tension à l'entrée analogique
    tension = entree_analogique.value * 3.3 / 65535
    print('tension: %5.3f V' % (tension), end='; ')
    # calculer la résistance de la thermistance
    r = Rpont * (3.3 / tension - 1)
    print('valeur resistance: %d Ohms' % (r), end='; ')
    # calculer l'angle par le modèle
    temperature = modele(r)
    # afficher l'angle avec l'unité
    print('temperature: %d deg C' % (temperature))
    # arrêter d'alimenter le montage
    alimentation.value = False
    # allumer la led en cyan (attente)
    led[0] = (0, 150, 255)
    # attendre 2s
    time.sleep(2)