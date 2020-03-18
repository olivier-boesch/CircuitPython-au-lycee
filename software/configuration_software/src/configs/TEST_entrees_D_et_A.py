from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import board
import time

d = []

d.append(DigitalInOut(board.D4))
d.append(DigitalInOut(board.D5))
d.append(DigitalInOut(board.D6))
d.append(DigitalInOut(board.D9))
d.append(DigitalInOut(board.D10))
d.append(DigitalInOut(board.D11))
d.append(DigitalInOut(board.D12))
d.append(DigitalInOut(board.D13))

a = []
a.append(AnalogIn(board.A0))
a.append(AnalogIn(board.A1))
a.append(AnalogIn(board.A2))
a.append(AnalogIn(board.A3))

for di in d:
    di.direction = Direction.INPUT
    di.pull = Pull.DOWN

print("ok")

while True:
    print("----")
    for di in d:
        print(di.value)
    for ai in a:
        print(ai.value)
    time.sleep(1)