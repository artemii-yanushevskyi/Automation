import os
import datetime
from time import sleep
def runfile(dir, interval, lasttime):
    backupproc = 'count.py'
    fulldir = os.path.join(dir, backupproc)
    delta = datetime.timedelta(minutes = interval)
    while True:
        if delta+lasttime > datetime.datetime.now():
            sleep(60*interval//2)
        else:
            break
    os.startfile(fulldir)

dir = os.getcwd()
print(dir)
interval = float(input('interval'))
dt = datetime.datetime.now()
runfile(dir, interval, dt)
