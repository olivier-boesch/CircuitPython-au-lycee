# -------------------------------
#
# GeoWave : Mesure de vitesse d'ondes sismiques
#
# Olivier Boesch - Lycée Saint Exupéry
# Marseille
#
# -------------------------------

# ------- imports --------
import board
import time
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from utilities import Notification, GREEN, ORANGE, RED, Button

# ---------- PARAMETRES ---------------

# Choix des broches
broche_depart =  board.A2
broche_arrivee = board.A3
broche_bouton_C = board.D5

# -------------------------------------

# --------- fonctions--------------
def config_bruit(entree):
    valeurs = []
    # relever 10 valeurs toutes les 10ms
    for i in range(10):
        valeurs.append(entree.value)
        time.sleep(0.01)
    bruit = sum(valeurs) / len(valeurs)  # moyenne des valeurs
    return max(bruit + 200, bruit * 1.2)  # 200 -> 10mV env ou +20% (arbritraire)

# ---------------------------------

# ---------- setup -------------
piezo_depart = AnalogIn(broche_depart)
piezo_arrivee = AnalogIn(broche_arrivee)
bouton_C = Button(broche_bouton_C, reverse=True)

notif = Notification()

# ------ logo ---------
notif.oled_logo('media/logo_stex.bin')
time.sleep(1)

# attente bouton C
notif.notify("Presser le bouton C\nPour demarrer\nune mesure", ORANGE)

# ---------- boucle -------------
while True:

    #attente du bouton
    while not bouton_C.check():
        pass

    # analyse du bruit ambiant et renoi de la limite
    limite_depart = config_bruit(piezo_depart)
    limite_arrivee = config_bruit(piezo_arrivee)

    notif.notify("attente d'une mesure\n............", GREEN)

    # attente de début de l'onde
    while piezo_depart.value < limite_depart:
        pass
    # stockage du temps
    start = time.monotonic_ns()

    # ----------- Propagation de l'onde --------------------

    # attente de fin de l'onde
    while piezo_arrivee.value < limite_arrivee:
        pass
    # stockage du temps
    end = time.monotonic_ns()

    notif.notify("Mesure :\nt = {:3.3f} ms\nPresser le bouton C".format((end - start) * 1000000), ORANGE)