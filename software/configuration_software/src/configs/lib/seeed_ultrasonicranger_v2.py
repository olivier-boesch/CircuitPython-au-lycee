# -------------------------------------------------------
# Librairie pour l'Ultrasonic Ranger V2 de Seeed
#
# Olivier Boesch - Lycée Saint Exupéry
# Marseille
#
# -------------------------------------------------------

# ------------ imports
import time
import pulseio
from digitalio import DigitalInOut, Direction

class UltrasonicRangerV2:
    def __init__(self, pin, speed_of_sound = 340.0):
        self._pin = pin
        self._speed_of_sound = speed_of_sound
        self._debug_hardware()

    def _debug_hardware(self):
        """debug_hardware : send a measure at startup to debug hardware"""
        # on envoie une impulsion de 5µs pour déclencher la mesure
        with DigitalInOut(self._pin) as pin:
            pin.direction = Direction.OUTPUT
            pin.value = False
            time.sleep(5e-6)
            pin.value = True
            time.sleep(5e-6)
        with pulseio.PulseIn(self._pin, maxlen=1) as pulses:
            pass

    def measure_time_ms(self):
        """measure_time : measure the time of flight of US wave. return as ms"""
        # on envoie une impulsion de 5µs pour déclencher la mesure
        with DigitalInOut(self._pin) as pin:
            pin.direction = Direction.OUTPUT
            pin.value = False
            time.sleep(5e-6)
            pin.value = True
            time.sleep(5e-6)
        # réception du retour
        # durée mesurée en µs correspondant au temps d'aller-retour de l'onde
        with pulseio.PulseIn(self._pin, maxlen=1) as pulses:
            # on attend l'impulsion
            while len(pulses) == 0:
                pass
            duration = pulses[0] / 1000.0  # calcul de la durée en ms
        return duration

    def measure_distance_cm(self):
        """Mesure time and convert to distance in cm"""
        duration = self.measure_time_ms()
        distance = duration * self._speed_of_sound * 10.0 / 2.0
        return distance