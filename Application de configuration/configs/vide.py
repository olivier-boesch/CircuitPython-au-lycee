import time
from utilities import Notification, GREEN, RED

notif = Notification()

while True:
    notif.notify(GREEN, 'Rien a faire...')
    time.sleep(1)
    notif.notify(RED, 'Je m\'ennuie...')
    time.sleep(1)