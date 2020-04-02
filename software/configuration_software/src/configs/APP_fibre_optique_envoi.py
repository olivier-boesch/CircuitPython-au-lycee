# -------------------------------------------
#
#  APP_fibre_optique_envoi
#
#  Envoi de données série par fibre optique
#
#  Olivier Boesch (c) 2020
#
# -------------------------------------------


# --------------- imports -------------------
import board  # définition des broches
import busio  # bus série
from digitalio import DigitalInOut, Direction  # entrées / sorties digitales
import time  # gestion du temps

# -------------- paramètres -----------------
# choisir une valeur dans la plage admise ( https://fr.wikipedia.org/wiki/UART#Vitesse_de_transmission )
# on peut choisir plus lent (en deça de 55 baud -> risque de plantage par saturation du buffer)
serial_speed = 55

# --------------- setup ---------------------
led = DigitalInOut(board.D13)  # led embarquée
led.direction = Direction.OUTPUT  # configuration en sortie
uart = busio.UART(board.TX, board.RX, baudrate=serial_speed)  # bus série (vitesse modifiable)

# ---------------- boucle (loop) ------------
while True:
    led.value = True  # allumage de la led embarquée -> début de transmission
    s = "Ceci est un test d'envoi {:f}".format(time.monotonic())  # envoi du temps interne
    data = uart.write(s.encode('utf-8'))  # encodage et envoi
    led.value = False  # extinction de la led embarquée -> fin de transmission
    time.sleep(5)  # attendre avant l'envoi du prochain message
