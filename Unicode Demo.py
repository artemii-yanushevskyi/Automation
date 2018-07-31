from __future__ import print_function
import io
from unicodedata import name, category
from curses.ascii import controlnames
from collections import Counter

try: # use these if Python 2
    unicode_chr, range = unichr, xrange
except NameError: # Python 3
    unicode_chr = chr

exclude_categories = set(('Co', 'Cn'))
counts = Counter()
control_names = dict(enumerate(controlnames))
with io.open('unidata', 'w', encoding='utf-8') as f:
    for x in range((2**8)**3): 
        try:
            char = unicode_chr(x)
        except ValueError:
            continue # can't map to unicode, try next x
        cat = category(char)
        counts.update((cat,))
        if cat in exclude_categories:
            continue # get rid of noise & greatly shorten result file
        try:
            uname = name(char)
        except ValueError: # probably control character, don't use actual
            uname = control_names.get(x, '')
            f.write(u'{0:>6x} {1}    {2}\n'.format(x, cat, uname))
        else:
            f.write(u'{0:>6x} {1}  {2}  {3}\n'.format(x, cat, char, uname))
# may as well describe the types we logged.
for cat, count in counts.items():
    print('{0} chars of category, {1}'.format(count, cat))
