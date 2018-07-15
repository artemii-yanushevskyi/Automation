import urllib.request
import sys
import ssl

# This restores the same behavior as before.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def report(blocknr, blocksize, size):
    current = blocknr*blocksize
    sys.stdout.write("\r{0:.2f}%".format(100.0*current/size))

def downloadFile(url):
    print("\n",url)
    fname = url.split('/')[-1]
    print(fname)
    # urllib.request.urlretrieve(url, fname, report)
    with urllib.request.urlopen(url, context=ctx) as u, open(fname, 'wb') as f:
        f.write(u.read())


def adapt(i, add_zero=False):
    if add_zero == True:
        if 0<=i<=9:
            r = '0' + str(i)
        else:
            r = str(i)
    else:
        r = str(i)
    return r

i = 1
try:
    while True:
        url = "http://http://www.matfiz.univ.kiev.ua/userfiles/files/Pres{}_cm.pdf".format(adapt(i))
        downloadFile(url)
        i += 1
except:
    print('number of lists is: '+str(i))
