import time

import board
import busio
import adafruit_bme280
from utilities import Notification, GREEN, BLUE

notif = Notification(always_led_on=True)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(notif.get_i2c(), 0x76)
serial = busio.UART(board.TX, board.RX, baudrate=115200)

bme280.mode = adafruit_bme280.MODE_NORMAL
bme280.standby_period = adafruit_bme280.STANDBY_TC_20
bme280.iir_filter = adafruit_bme280.IIR_FILTER_X2
bme280.overscan_pressure = adafruit_bme280.OVERSCAN_X16
bme280.overscan_humidity = adafruit_bme280.OVERSCAN_X2
bme280.overscan_temperature = adafruit_bme280.OVERSCAN_X1
# The sensor will need a moment to gather initial readings
time.sleep(1)

while True:
    notif.led(BLUE)
    notif.oled_text(
        "Temperature: {:0.1f} C\nHumidity: {:0.1f} %\nPressure: {:0.1f} hPa".format(bme280.temperature, bme280.humidity,
                                                                                    bme280.pressure))
    buf = bytes("Température:{:0.1f},Humidité:{:0.1f},Pression:{:0.1f}\n".format(bme280.temperature, bme280.humidity,
                                                                                 bme280.pressure), "utf8")
    serial.write(buf)
    notif.led(GREEN)
    time.sleep(1)
