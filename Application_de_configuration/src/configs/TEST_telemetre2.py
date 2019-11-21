# -------------------------------------------------------
# Télémètre
#
# Olivier Boesch - Lycée Saint Exupéry
# Marseille
#
# -------------------------------------------------------

# ------------ imports
import board
import time
from utilities import Notification, Button
import pulseio
import array
from digitalio import DigitalInOut, Direction

# ------------ parametres ----------
broche_US = board.D12
broche_ButC = board.D5
broche_activite = board.D13
# -------------------------------------------------------

# ------------- setup
# ecran oled ou port série pour l'affichage
notif = Notification()
# bouton pour déclencher la mesure
butC = Button(broche_ButC, reverse=True)
# led d'activité
led = DigitalInOut(broche_activite)
led.direction = Direction.OUTPUT

# afficher le logo mep au démarrage
notif.oled_logo('media/logo_mep.bin')
time.sleep(1)

# inviter l'utilisateur à appuyer sur le bouton C
notif.notify("Veuillez appuyer\nsur le bouton C\npour faire une mesure")


# -------------- boucle (loop)
while True:
    # attente d'un appui sur le bouton C pour déclencher la mesure
    butC.check()
    while not butC.is_pushed():
        time.sleep(0.2)
        butC.check()

    # envoi du déclenchement de la mesure
    led.value = True  # on allume la led13 (rouge) pour indiquer le début la mesure
    # on envoie une impulsion de 2ms (2000µs) pour déclencher la mesure
    with DigitalInOut(broche_US) as pin:
        pin.direction = Direction.OUTPUT
        pin.value = False
        time.sleep(2e-6)
        pin.value = True
        time.sleep(5e-6)
        pin.value = False
        time.sleep(2e-6)

    # réception du retour
    # durée mesurée en µs correspondant au temps d'aller-retour de l'onde
    with pulseio.PulseIn(broche_US, maxlen=2) as p:
        # on attend l'impulsion
        while len(p) == 0:
            pass
        led.value = False  # on éteint la led -> fin de mesure
        t = p[0] / 1000.0  # calcul de la durée en ms
        d = p[0] / 1000000 * 342.0 / 2.0  # calcul de la distance en m
    # afffichage sur l'écran oled ou le port série
    res = "t = {:3.2f} ms \n d = {:3.2f} m".format(t,d)
    notif.notify(res)
