from selenium import webdriver
import time


class Webpage:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.get(url)


class Youtube(Webpage):
    def loadEntirePage(self):
        while True:
            time.sleep(9)
            try:
                response = self.driver.execute_script(
                    "document.getElementsByClassName"
                    "('load-more-button')[0].click()")
            except:
                print('done!')
                break


if __name__ == '__main__':
    likedVideos = Youtube(
        'https://www.youtube.co.uk/playlist?list=LLvI2sZXK-MUg5fsusK3l4LA')
    # likedVideos.loadEntirePage()


# driver.get('https://www.youtube.co.uk/playlist?list=LLvI2sZXK-MUg5fsusK3l4LA')
# buttonLoadMore = driver.find_element_by_xpath('//*[@id="pl-video
# -list"]/button')
# buttonLoadMore = driver.find_element_by_class_name('load-more-button')
# buttonLoadMore.click()
# window.scrollTo(0, document.body.scrollHeight); document.
# getElementsByClassName('load-more-button')[0].click() // document.
# getElementsByClassName('button')[0].click(); ''')
