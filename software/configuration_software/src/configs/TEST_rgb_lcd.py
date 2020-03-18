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
import grove_RGB_LCD

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
big_lcd = grove_RGB_LCD.rgb_lcd(16,2,shared_i2c = notif.get_i2c())
big_lcd.print('Hello !')
big_lcd.setRGB(255,255,0)
big_lcd.print('Hello !')

# ---------- boucle -------------
while True:
    # recupérer la mesure du capteur
    notif.notify(str(capteur_pression.get_pressure())+' Pa')
    big_lcd.print(str(capteur_pression.get_pressure())+'Pa')
    time.sleep(0.2)