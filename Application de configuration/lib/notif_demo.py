from utilities import Notification, RED, GREEN, YELLOW, PURPLE, CYAN
import time

notif = Notification()

while True:
    notif.notify(color=GREEN, text='you can write\n3 lines\nof text (20c/line)')
    time.sleep(2)

    notif.notify(color=PURPLE, text='1234567890abcdefghijk\n1234567890abcdefghijk\n1234567890abcdefghijk')
    time.sleep(2)

    notif.notify(color=GREEN, text='you will see\na logo loaded\nfrom a file')
    time.sleep(2)

    notif.show_logo('saintex_logo.bin')
    time.sleep(1)

    notif.notify(color=CYAN, text='an horizontal\nprogress bar running\nvery slow :(')
    time.sleep(2)

    for i in range(0, 101, 10):
        notif.oled_bar(i)
    time.sleep(2)

    notif.notify(color=RED, text='end of demo\nbye..........')
    time.sleep(2)

    for i in range(5, -1, -1):
        notif.notify(color=YELLOW, text='end of demo\nbye\nrestart in {}...'.format(i))
        time.sleep(0.5)
