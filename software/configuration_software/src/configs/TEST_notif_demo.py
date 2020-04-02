# --------------------------------------------------------------------------------
#  Notification demo
#
#
#
#
# --------------------------------------------------------------------------------

from utilities import Notification, BLUE, RED, GREEN, YELLOW, PURPLE, CYAN
import time

notif = Notification(always_led_on=True, led_brightness=0.8)

while True:
    # text demo
    notif.notify(color=GREEN, text='you can write\n3 lines\nof text (20c/line)')
    time.sleep(2)

    notif.notify(color=PURPLE, text='1234567890abcdefghijk\n1234567890abcdefghijk\n1234567890abcdefghijk')
    time.sleep(2)

    # logo demo
    notif.notify(color=GREEN, text='you will see\nthree logos loaded\nfrom files')
    time.sleep(2)

    notif.oled_logo('media/logo_test.bin')
    notif.led(color=PURPLE)
    time.sleep(1)

    notif.oled_logo('media/logo_stex.bin')
    notif.led(color=YELLOW)
    time.sleep(1)

    notif.oled_logo('media/logo_mep.bin')
    notif.led(color=BLUE)
    time.sleep(1)

    # progress bar demo
    notif.notify(color=CYAN, text='an horizontal\nprogress bar running')
    time.sleep(1)

    for i in range(0, 101, 10):
        notif.oled_bar(i)
        notif.led(color=(int(i * 2.55), 255 - int(i * 2.55), 50))
    time.sleep(2)

    # end
    notif.notify(color=GREEN, text='end of demo\nbye..........')
    time.sleep(2)

    for i in range(5, -1, -1):
        notif.notify(color=(0, 0, 255 - int((5 - i) * 51)), text='end of demo\nbye\nrestart in {}...'.format(i))
        time.sleep(0.5)
