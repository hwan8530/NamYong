# Crawling Interface

from urllib.request import urlopen
from bs4 import BeautifulSoup

class Crawling() :
    url = ""
    html = ""
    source = ""
    soup = ""
    def __init__(self, url):
        self.url = url
        self.html = self.openUrl(self.url)
        self.source = self.getSource()
        self.soup = self.getSoup(self.source)

    def openUrl(self, url):
        return urlopen(url)

    def getSource(self):
        return self.html.read()

    def getSoup(self, source):
        self.soup = BeautifulSoup(source,"html.parser")
