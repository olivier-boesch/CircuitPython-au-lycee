# -------------------------------------------
#
#  APP_fibre_optique_reception
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
lines_count = 0  # ligne actuelle de l'écran
s=''  # texte à afficher


# ---------------- boucle (loop) ------------
while True:
    led.value = True  # allumage de la led embarquée -> début de transmission et affichage
    data = uart.read(13)  # lire 13 caractères en une fois (une ligne de l'écran)
    if data is not None:  # quelque chose a été lu ?
        s += data.decode('utf-8') + '\n'  # décodage vers utf8 et ajout de la ligne
        lines_count += 1
        if line_current == 4:  # trop de lignes ?
            s = s[12:]  # enlever la ligne la plus ancienne
            lines_count -= 1
        notif.notify(text=s)
    led.value = False  # extinction de la led embarquée -> fin de transmission et affichage

