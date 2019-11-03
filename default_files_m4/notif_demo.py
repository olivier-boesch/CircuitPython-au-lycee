from utilities import Notification, RED, GREEN, YELLOW, PURPLE, CYAN, Button
import time
import board

# notification object
n = Notification(always_serial_output=True)
# Buttons
but_A = Button(board.D9, True)
but_B = Button(board.D6, True)
but_C = Button(board.D5, True)

while True:
    # text display
    n.notify(color=GREEN, text='you can write\n3 lines\nof text (21c/line)')
    time.sleep(2)
    n.notify(color=PURPLE, text='1234567890abcdefghijk\n1234567890abcdefghijk\n1234567890abcdefghijk')
    time.sleep(2)
    # logo display
    n.notify(color=GREEN, text='you will see\na logo loaded\nfrom a file')
    time.sleep(2)
    n.oled_logo('logo.bin')
    time.sleep(2)
    # progress bar display
    n.notify(color=CYAN, text='an horizontal\nprogress bar running\nvery slow :(')
    time.sleep(2)
    for i in range(0, 101, 5):
        n.oled_bar(i)
    time.sleep(2)
    # button watch
    n.notify(color=CYAN, text='Now it\'s time\nto test\nthe buttons (10s)')
    time.sleep(2)
    time_start = time.monotonic()
    #loop for 15s
    while time.monotonic() - time_start < 15.0:
        s = " "
        but_A.check()
        but_B.check()
        but_C.check()
        if but_A.is_pushed():
            s += 'A,'
        if but_B.is_pushed():
            s += 'B,'
        if but_C.is_pushed():
            s += 'C,'
        n.notify(text="Button pressed\n"+s[:-1])
    # prepare for restart
    n.notify(color=RED, text='end of demo\nbye..........')
    time.sleep(2)
    for i in range(5, -1, -1):
        n.notify(color=YELLOW, text='end of demo\nbye\nrestart in {}...'.format(i))
        time.sleep(0.5)