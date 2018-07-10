# Find the Oldest File
''' Скласти програму, яка знаходить у каталозі та його
підкаталогах «найстарший» файл, тобто файл, створений раніше за
інших.
'''
from time import time
import os
catalog = 'cat'
from time import time
time = time()
oldest = None
for root, dirs, files in os.walk(catalog):
    for file in files:
        timeFile = os.path.getctime(os.path.join(root, file))
        if timeFile < time:
            oldest, time = os.path.join(root, file), timeFile
print(oldest)
print(time.ctime(time))
