# Crawling Interface
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

class Crawling() :
    url = ""
    html = ""
    soup = ""
    option = ""
    driver = ""

    def __init__(self, url):
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('headless')
        self.option.add_argument('window-size=1920x1080')
        self.option.add_argument("disable-gpu")
        self.driver = webdriver.Chrome('./chromedriver', chrome_options=self.option)

    def waitForLoad(self):
            self.driver.implicitly_wait(3)
        # This method needs to override

    def getHtml(self):
            self.html = self.driver.page_source

    def parseSoup(self):
            self.soup = BeautifulSoup(self.html, 'html.parser')

