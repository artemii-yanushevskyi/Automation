import os, re
import time
from datetime import date

# >>> time.ctime(1519821827.790685)
# 'Wed Feb 28 13:43:47 2018'



for root, dirs, files in os.walk('.'):
    print(root, dirs)
    for file in files:
        # print(file)
        d = re.search('^(\d\d\d\d)-(\d\d)-(\d\d)', file)
        if d:
            d = date(int(d.group(1)),int(d.group(2)),int(d.group(3)))
            # print(time.mktime(d.timetuple()))
            os.utime(file, (time.mktime(date(1999,1,1).timetuple()), time.mktime(d.timetuple()))) # make it to work in directories
            # print(time.ctime(time.mktime(d.timetuple())))
            os.rename(file, file[13:])
