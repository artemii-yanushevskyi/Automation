# https://www.memrise.com/course/131111/5000-most-common-french-words/1/
import os
from urllib.request import urlopen
import ssl

from bs4 import BeautifulSoup

# This restores the same behavior as before.
context = ssl._create_unverified_context()

for i in range(1,51):
    url = 'https://www.memrise.com/course/131111/5000-most-common-french-words/{}/'.format(str(i))
    response = urlopen(url, context=context).read()
    decoded_html = response.decode('utf-8')

    soup = BeautifulSoup(decoded_html, "html.parser")


    dictionary = {}
    i = 0
    for item in soup.find_all("div", class_="text"):
        if len(item["class"]) != 1:
            if i == 0:
                key = item.text
                i = 1
            else:
                definition = item.text
                i = 0
                dictionary[key] = definition

    text = ''
    for key, value in dictionary.items():
        text += key + ' --- ' + value + "\n"

    text += "\n"
    
    with open("5453 les mots populaires.txt", "ab") as f:
       f.write(text.encode("UTF-8"))

    print(i)

'''
save raw html to a file:

for i in range(1,4):
    url = 'https://www.memrise.com/course/131111/5000-most-common-french-words/{}/'.format(str(i))
    response = urlopen(url, context=context).read()
    decoded_html = response.decode('utf-8')
    
    with open("file.txt", "ab") as f:
       f.write(decoded_html.encode("UTF-8"))

'''
