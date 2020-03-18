# -------------------------------------------------------
#  
# Affichage logo simple
#
#  Olivier Boesch (c) 2019
#
# -------------------------------------------------------

from utilities import Notification, BLUE
# ------------ parametres ----------
# -------------------------------------------------------

# ------------- setup
# affichage logo et led blue
notif = Notification(always_led_on=True, led_brightness=0.7)
notif.led(BLUE)
notif.oled_logo('media/logo_mep.bin')

# -------------- boucle (loop)
while True:
    pass
