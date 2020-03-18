# -------------------------------
#
# Pressiometre
#
# Olivier Boesch - Lycée Saint Exupéry
# Marseille
#
# -------------------------------

# ------- imports --------
import board
import time
from analogio import AnalogIn
from utilities import Notification
import integrated_pressure_sensor_kit

# ---------- PARAMETRES ---------------
# -------------------------------------

# ------- Choix des broches -----------
broche_cap =  board.A2

# ---------- setup -------------
notif = Notification()
capteur_pression = integrated_pressure_sensor_kit.IntegratedPressureSensorKit(pin_sensor=broche_cap,offset=-2.49090371e4)

# ------ logo ---------
notif.oled_logo('media/logo_mep.bin')
time.sleep(1)

# ---------- boucle -------------
while True:
    # recupérer la mesure du capteur
    notif.notify("Pression : {:4.0f} Pa".format(capteur_pression.get_pressure()))
    time.sleep(0.5)