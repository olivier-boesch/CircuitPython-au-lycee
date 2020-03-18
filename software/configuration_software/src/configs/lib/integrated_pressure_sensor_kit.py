import board
import time
from analogio import AnalogIn

class IntegratedPressureSensorKit:
    """IntegratedPressureSensorKit: Helper class to experiment with Seed Integrated Pressure Sensor Kit v1.0
        parameters:
            pin_sensor: board pin of the sensor (defaults to A0)
            offset : offset value (defaults to -31109.0371 - see note below)
            slope : slope value (defaults to 11.1652778 - see note below)
            nb_readings : number of readings to calculate mean (defaults to 10)
            ----
            sensor transfer function: the relation is (almost) linear
                as P = raw_value * slope + offset
                P is in pascal
                raw_value is the analog input value (0-65535)
                slope and offset are calculated with the formulas :
                slope = 1000*Vcc/(N*c*Vs*a)
                offset = - 1000*b/a
                where Vcc = 3.3V (Vcc of python µC); N = 2**16-1 = 65535 (resolution of analog input);
                c = 4700/(2000+4700) = 0.7015 (conversion factor made by the sensor - see kit schematic);
                Vs = 5V (Vcc for the sensor - see kit schematic); a = 0.0012858 (sensor slope - see sensor datasheet);
                b = 0.04 (sensor offset - see sensor datasheet)
                kit schematic : http://wiki.seeedstudio.com/Grove-Integrated-Pressure-Sensor-Kit/
                sensor datasheet : http://www.meditronik.com.pl/doc/b0-b9999/mpx5700.pdf
                """
    def __init__(self, pin_sensor=board.A0, slope=11.1652778, offset=-31109.0371, nb_readings=10):
        self.sensor = AnalogIn(pin_sensor)
        self.offset = offset
        self.slope = slope
        self.nb_readings = nb_readings

    def get_raw_value(self):
        """returns the mean of raw values after read nb_readings and calculate mean"""
        raw_value = 0
        for i in range(self.nb_readings):
            raw_value += self.sensor.value
        return raw_value / self.nb_readings

    def get_voltage(self):
        return self.get_raw_value()*3.3/65535

    def get_voltage_sensor(self):
        return self.get_voltage()/0.7015

    def get_pressure(self):
        """returns the calculated pressure in Pa with the mean of nb_readings"""
        P = self.get_raw_value() * self.slope + self.offset
        return P