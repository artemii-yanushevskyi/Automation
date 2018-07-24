# https://www.memrise.com/course/131111/5000-most-common-french-words/1/
import os
from urllib.request import urlopen
import ssl

from bs4 import BeautifulSoup

# This restores the same behavior as before.
context = ssl._create_unverified_context()

url = 'http://www.le-francais.ru/bibliotheque/adopte'
response = urlopen(url, context=context).read()
decoded_html = response.decode('utf-8')

soup = BeautifulSoup(decoded_html, "html.parser")

dictionary = {}
i = 'translation'
ready = False
for item in soup.find_all("td"):
    if ready == True:
        if i == 'translation':
            trans = item
            i = 'original'
        elif i == 'original':
            orig = item
            i = 'explanation'
        else:
            dictionary[orig] = [trans, item]
            i = 'translation'
            # print(orig.text, trans.text, item.text)
    elif item.text == 'абажур ':
        trans = item
        i = 'original'
        ready = True


text = ''

for key, value in dictionary.items():
    line = key.text + ' --- ' + value[0].text + ' •Explication: ' + value[1].text
    text += line + "\n"
    # print(line)


with open("results/Rus-Fr Dictionary.txt", "ab") as f:
    f.write(text.encode("UTF-8"))


