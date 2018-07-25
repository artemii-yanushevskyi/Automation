# https://www.memrise.com/course/131111/5000-most-common-french-words/1/
import os
from urllib.request import urlopen
import ssl

from bs4 import BeautifulSoup

# This restores the same behavior as before.
context = ssl._create_unverified_context()

url = "https://aeon.co/essays/your-brain-does-not-process-information-and-it-is-not-a-computer"
response = urlopen(url, context=context).read()
decoded_html = response.decode('utf-8')

with open("webpage.html", "wb") as f:
   f.write(decoded_html.encode("UTF-8"))


