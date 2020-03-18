# -------------------------------------------------------
#   APP_mecanique
#
#   Mesure de vitesse d'une bille sur plan incliné
#
#   Olivier Boesch (c) 2020
# -------------------------------------------------------


# ------------ imports --------------
import board  # définition des broches
import time  # gestion du temps
from utilities import Notification, BLUE, GREEN, YELLOW, RED, WHITE  # gestion de l'écran et des échanges de données
from galilee import Galilee
from analogio import AnalogIn


# ------------ parametres ----------
# broches des capteurs à adapter suivant les besoins (sur le même port grove !)
# D4/D5 , D6/D9, D10/D11 ou D12/D13
broche_capteur1 = board.D4
broche_capteur2 = board.D5
temps_max_mesure = 3.0  # s - durée max de mesure


# ------------- setup --------------
# init galilee
galilee = Galilee(pin_sensor1=broche_capteur1, pin_sensor2=broche_capteur2, timeout=temps_max_mesure)
# config des notifications
notif = Notification(always_led_on=True)
# affichage du logo
notif.intro()
# texte initial
notif.notify(color=WHITE, text="\nattente de mesure...")


# -------------- boucle (loop) ------
while True:
    duree = galilee.capture()
    if duree is None:
        notif.notify(color=YELLOW, text="mesure non valide\nattente de mesure...")
    else:
        notif.led(color=GREEN)
        time.sleep(0.1)
        notif.notify(color=WHITE, text="duree:\n{:2.3f} ms".format(duree/1000))  # affichage en ms