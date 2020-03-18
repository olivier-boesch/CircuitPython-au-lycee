import board
import busio
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

uart = busio.UART(board.TX, board.RX, baudrate=110)

while True:
    led.value = True
    data = uart.write(b"it is ok !")  # read up to 32 bytes
    # print(data)  # this is a bytearray type
    led.value = False
    time.sleep(1)