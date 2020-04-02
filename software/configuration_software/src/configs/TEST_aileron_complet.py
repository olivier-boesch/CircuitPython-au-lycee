import board
from analogio import AnalogIn
import time
from utilities import Notification
from digitalio import DigitalInOut, Direction

# ------------ parametres (pour le professeur) ----------
broche_entree = board.A3  # broche d'entree du potentiomètre
broche_led = board.D4


# -------------------------------------------------------


# ################## MODELES A MODIFIER PAR L'ELEVE ###########################
# calcul de la résistance
def calcul_resistance(u):
    r = (3.3 / u - 1.0) * 47000.0 - 110.0
    return r


# calcul de l'angle
def calcul_angle(R):
    ang = 300 / 52000 * R - 150.0
    return ang


# ############################################################################


# configuration de l'entrée analogique
entree_analogique = AnalogIn(broche_entree)
# configuration de la sortie de la led
led = DigitalInOut(broche_led)
led.direction = Direction.OUTPUT  # c'est une sortie
# config des notifications
notif = Notification()
# show logo at startup
notif.oled_logo('media/logo_mep.bin')
time.sleep(5)

# boucle
while True:

    # récupérer la valeur de l'entrée (16bits) calculer la tension à l'entrée analogique
    tension = entree_analogique.value * 3.3 / 65535
    # calculer la résistance du potentiomètre
    r = calcul_resistance(tension)
    # calculer l'angle par le modèle
    angle = calcul_angle(r)
    # afficher la mesure
    notif.notify(text='Ur={:3.3f}V\nr={:3.0f}Ohms\na={:3.0f}deg'.format(tension, r, angle))
    # sortie sur la liaison série avec l'ordinateur (angle seul)
    print("({:3.0f})".format(angle))
    # détection d'un angle trop grand -> problème !
    if angle > 40.0 or angle < -40.0:
        led.value = True  # on allume la led
    else:
        led.value = False  # tout va bien -> on éteint la led
