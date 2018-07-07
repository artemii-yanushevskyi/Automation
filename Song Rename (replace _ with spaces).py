import os, re
replace = lambda s: ' '.join(v for v in s.split('_'))
c = os.listdir()
for m in c:
    print(m)
    if re.match('^.*\.mp3$', m):
        print('ff')
        newName = replace(m)
        os.rename(m, newName)
