# -------------------------------------------------------
#
#
#
#
#
# -------------------------------------------------------

# ------------ imports
import board
import time
import neopixel
from utilities import RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, ORANGE, OFF
# ------------ parametres ----------
# -------------------------------------------------------

# ------------- setup
# configuration de la led neopixel
neopixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.8, auto_write=True)

# -------------- boucle (loop)
while True:
    neopixel.fill(RED)
    time.sleep(0.5)
    neopixel.fill(YELLOW)
    time.sleep(0.5)
    neopixel.fill(GREEN)
    time.sleep(0.5)
    neopixel.fill(CYAN)
    time.sleep(0.5)
    neopixel.fill(BLUE)
    time.sleep(0.5)
    neopixel.fill(PURPLE)
    time.sleep(0.5)
    neopixel.fill(ORANGE)
    time.sleep(0.5)
    neopixel.fill(OFF)
    time.sleep(0.5)