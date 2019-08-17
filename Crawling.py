# Crawling Interface
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Crawling() :
    url = ""
    html = ""
    source = ""
    soup = ""
    option = ""
    driver = ""

    def __init__(self, url):
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('headless')
        self.option.add_argument('window-size=1920x1080')
        self.option.add_argument("disable-gpu")
        self.driver = webdriver.chrome('./chromedriver', chrome_options=self.option)
        self.driver.get(url)
        self.html = self.driver.page_source
        self.soup = BeautifulSoup(self.html, 'html.parser')

