# that is a bot to automate vk login
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
def getPassword():
    import getpass
    return getpass.getpass('Password: ')
# test 0
class LoginTest(unittest.TestCase):
    def setUp(self):
        # import chrome options
        chromeOptions = webdriver.ChromeOptions()
        # setting option to open incognito window
        chromeOptions.add_argument("--incognito")
        # running with option
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        # load page
        self.driver.get("http://vk.com/")
    def testLogin(self):
        driver = self.driver
        email = input('Print your email: ')
        password = getPassword()
        emailFieldID = "index_email" # that's id
        passFieldID = "index_pass" # that's id also
        loginButton = "//button[contains(@id ,'index_login_button')]" # id
        # myNameXpath = "//h2[contains(. , 'Artemy  Yanushevsky')]" # @ instead . for attribute
        # wait for my name to apper
        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButton))
        # entering mail
        emailFieldElement.clear()
        emailFieldElement.send_keys(email)
        # entering password
        passFieldElement.clear()
        passFieldElement.send_keys(password)
        # clicking the button
        loginButtonElement.click()
        # waitiong for my name to appear
        import time
        time.sleep(3)
        waitForHtmlTag = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath('//html'))
        driver.get('http://vk.com/id1')
        waitForHtmlTag = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath('//html'))
    def tearDown(self):
        self.driver.quit()

# main
if __name__ == '__main__':
    unittest.main()
