import re, os
import mmap

print('Start...')
catalog = '.' # '/' - from the root, 'cat', '.' - in file's directory
patterns = {r'<=>':"$\\\\Leftrightarrow$",r'<=':"$\\\\Leftarrow$",r'=>':"$\\\\Rightarrow$",r'\|->':"\\\\mapsto ",r'->':'\\\\rightarrow ',}
for (dirpath, dirnames, filenames) in os.walk(catalog):
    for filename in filenames:
        print('File under consideration', filename)
        name = re.search('\.(.+)$', filename)
        if name.group(1) == 'tex':
            import io
            with io.open(os.path.join(dirpath, filename), 'r', encoding='utf-8', errors='replace') as file:
                text = file.read()
            print('- recognized and open an applicable file')
            for pattern, replacement in patterns.items():
                pattern = re.compile(pattern, flags=0)
                textnew = re.sub(pattern, replacement, text)
                text = textnew
                print('replacement', str(pattern), replacement)
            print(text)
            file = open(os.path.join(dirpath, filename+'.re.tex'), 'wb')
            file.write(text.encode('utf8'))
            file.close()
        else:
            print('File {} doest\'t match a criteria and is rejected'.format(filename))

