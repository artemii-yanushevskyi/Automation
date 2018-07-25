# visit github page of this project
from bs4 import BeautifulSoup
import urllib.request


class Webpage:
    def __init__(self, url):
        self.url = url
        page = urllib.request.urlopen(url)
        self.content = page.read()
        page.close()

    def makeBS(self):
        return BeautifulSoup(self.content, "lxml")

i = 22
f = open("page2", 'a')

for i in range(1, 244):
    link = "http://www.testpreppractice.net/GRE/awa-samples/gre-issue-essay-{}.html".format(i)
    # print(link)
    page = Webpage(link)
    soup = page.makeBS()

    search = soup.find('div', {'id': 'content'})
    search2 = search.find_all()

    no_links = []

    
    for p in search2:
        if p.find_all('a') == []:
            no_links.append(p.get_text())

    text = "\n".join(no_links)
    print(text, file = f)

f.close()

    #wp = Webpage

##class Youtube(Webpage):
##    def loadEntirePage(self):
##        while True:
##            time.sleep(9)
##            try:
##                response = self.driver.execute_script(
##                "document.getElementsByClassName"
##                "('load-more-button')[0].click()")
##            except:
##                print('done!')
##                break
##
##
##likedVideos = Youtube(
##    'https://www.youtube.co.uk/playlist?list=LLvI2sZXK-MUg5fsusK3l4LA')
### likedVideos.loadEntirePage()
##html = likedVideos.driver.page_source
##soup = BeautifulSoup(html, 'lxml')
##videos = soup.find_all("tr", {"class": "pl-video"})
##
##
##
##class Video:
##    url = 'http://youtube.co.uk/'
##
##    def __init__(self, video):
##        self.element = video
##        self.name = None
##        self.length = '0'
##        self.publisher = 'Unknown'
##        self.url = Video.url
##        self.getName()
##        self.getParameters()
##
##    def getName(self):
##        self.name = self.element.get('data-title')
##        print(self.name)
##        self.url = Video.url + 'watch?v=' + self.element.get('data-video-id')
##
##    def getParameters(self):
##        children = self.element.findChildren()  # get all children, grandchi..
##        for child in children:
##            if child.get('class'):
##                if 'pl-video-title' in child.get('class'):
##                    # print('pl-video-title')
##                    pass
##                if 'timestamp' in child.get('class'):
##                    timeChild = child.findChildren()[0]
##                    self.length = timeChild.contents[0]
##            if child.get('data-name') and child.get('class'):
##                if 'spf-link' in child.get('class') and \
##                        'playlist' in child.get('data-name'):
##                    self.publisher = child.contents
##                    self.publisher = self.publisher[0]
##
##    def reveal(self):
##        print(self.url, self.name, self.length, self.publisher)
##
##
##videoClass = {}
##for video in videos:
##    v = Video(video)
##    fieldsV = v.__dict__
##    fieldsV.pop('element')  # waaay to long
##    videoClass.update({fieldsV['name']: fieldsV})
### make xml file
##f = open('videos1.xml', 'w')
##print(dictionaryToXML(videoClass), file=f)
##f.close()