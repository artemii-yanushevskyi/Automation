"""get voice memos from iPhone with http://dl.i-funbox.com then rename them with
this script #recordings #voice memos"""

import codecs
f = codecs.open("AssetManifest.plist", "r", "utf-8")
xml = f.read()
d = {}
import re, os
xml = xml.split("\n")
for line in xml:
    reg1 = "<key>(.*)\.m4a</key>"
    reg2 = "<string>(.*)</string>"
    try:
        result = re.search(reg1, line)
        print(result.group(1))

        name = result.group(1)+".m4a"
    except:
        pass

    try:
        result = re.search(reg2, line)
        print(result.group(1))

        myname = result.group(1)

        d[name] = myname
        
        print("dictionary" + name + myname)
        os.rename(name, myname+".m4a")
    except:
        pass
    
