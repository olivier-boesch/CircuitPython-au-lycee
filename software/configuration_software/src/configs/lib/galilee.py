import board
import time
from digitalio import DigitalInOut, Direction

class Galilee:
    """Galilee: Helper class to experiment with galilee
        parameters:
            pin_sensor1: board pin of the first sensor (defaults on D4)
            pin_sensor2: board pin of the second sensor (defaults on D5)
            timeout: timeout in seconds before discarding capture on  sensor 2 (defaults to 2s)"""
    def __init__(self, pin_sensor1=board.D4, pin_sensor2=board.D5, timeout=2):
        self.sensor1 = DigitalInOut(pin_sensor1)
        self.sensor1.direction = Direction.INPUT
        self.sensor2 = DigitalInOut(pin_sensor2)
        self.sensor2.direction = Direction.INPUT
        self.timeout = timeout*1000000000  # convert timeout from s to ns

    def capture(self):
        """returns duration as ms as an int or None if a timeout has happened"""
        # wait for sensor1
        time1 = time.monotonic_ns()
        while not self.sensor1.value:
            time1 = time.monotonic_ns()
        # wait for sensor2 or timeout
        time_stop = time1 + self.timeout
        time2 = time.monotonic_ns()
        while not self.sensor2.value and time2 < time_stop:
            time2 = time.monotonic_ns()
        # timeout -> return None
        if time2 >= time_stop:
            return None
        # no timeout -> return duration in µs (since time.monotonic_ns is not quite precise) as an int
        else:
            return int((time2 - time1) / 1000)