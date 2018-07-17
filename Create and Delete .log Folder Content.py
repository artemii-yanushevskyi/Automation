import datetime
import os

catalog = 'folder'

def makeLogs(n):
    '''make log files'''
    for root, dirs, files in os.walk(catalog):
        for dir in dirs:
            log = open(os.path.join(root, dir, 'journal{}.log'.format(n)), 'w')
            listElements = os.listdir(os.path.join(root, dir))
            print(listElements, file = log)
            log.close()
            
def delLogs():
    '''delete old log files'''
    for root, dirs, files in os.walk(catalog):
        for dir in dirs:
            listElements = os.listdir(os.path.join(root, dir))
            for file in listElements:
                name = re.search('journal(\d+)\.log', file)
                
while True:
    sleep(60*interval//2)
    makeLogs(1)

