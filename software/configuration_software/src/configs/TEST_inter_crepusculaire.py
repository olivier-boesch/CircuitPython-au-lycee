# -------------------------------
#
# inter crepusculaire
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
from utilities import Notification, GREEN, RED

# ---------- PARAMETRES ---------------

# Valeur de la résistance du pont
r_pont = 10000.0  # Ohms

# Valeur max de la resistance du capteur pour led eteinte
limit = 20000.0 # Ohms

# -------------------------------------

# Choix des broches
broche_cap =  board.A0
broche_led = board.D4


# ---------- setup -------------
capteur = AnalogIn(broche_cap)
led = DigitalInOut(broche_led)
led.direction = Direction.OUTPUT
notif = Notification()

# ------ logo ---------
notif.oled_logo('media/logo_stex.bin')
time.sleep(1)

# ---------- boucle -------------
while True:
    # recupérer la mesure du capteur
    mesure_cap = capteur.value

    u_cap = mesure_cap * 3.3 / 65535.0;

    r_cap = (3.3 / u_cap -1.0) * r_pont;

    if r_cap < limit:
        led.value = False
        notif.notify("Il fait jour !\nu_cap = {:3.2f} V\n r_cap = {:5.1f} Ohms".format(u_cap, r_cap), GREEN)
    else:
        led.value = True
        notif.notify("Il fait nuit !\nu_cap = {:3.2f} V\n r_cap = {:5.1f} Ohms".format(u_cap, r_cap), RED)

    time.sleep(0.1)  # attendre 0.1s
