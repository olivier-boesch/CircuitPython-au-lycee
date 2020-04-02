# -------------------------------------------------------
# Télémètre
#
# Olivier Boesch - Lycée Saint Exupéry
# Marseille
#
# -------------------------------------------------------

# ------------ imports
import time
from utilities import Notification, SoundGenerator

# ------------ Paramètres
frequence = 440  # Hz - fréquence du son généré
# Attention : fréquence de rendu à 35535 Hz max...

# ------------- setup
# ecran oled ou port série pour l'affichage
notif = Notification()

# générateur de sons
sound_gen = SoundGenerator(frequency=frequence, sampling_frequency=16000, stereo=True)

# afficher le logo mep au démarrage
notif.oled_logo('media/logo_mep.bin')
time.sleep(1)

# -------------- boucle (loop)
while True:
    sound_gen.play()
    time.sleep(1)
    sound_gen.stop()
    time.sleep(1)
    sound_gen.bip()
    time.sleep(1)
    sound_gen.bip()
    time.sleep(1)
    sound_gen.bip()
    time.sleep(1)
