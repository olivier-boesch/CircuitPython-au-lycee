import time
from utilities import Notification, GREEN, RED

notif = Notification()

while True:
    notif.notify(color=GREEN, text='Rien a faire...')
    time.sleep(1)
    notif.notify(color=RED, text='Je m\'ennuie...')
    time.sleep(1)