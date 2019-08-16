from bs4 import BeautifulSoup
from Crawling import *

class Gmarket(Crawling) :
    def __init__(self, url):
        super().__init__(url)

    def getSoup(self, source):
        return BeautifulSoup(source, "html.parser")

    # 상품정보 가지고있는 모든 div
    def all_Item(self):
        return self.soup.find_all(class_="item_info")

    def item_info(self):
        tables = (self.soup.find_all(class_ = "item_info"))
        # tables = (self.soup.select("div.item_info")).parent
        # names = self.soup.select("div.item_info > a > span.title")
        iteminfo = []

        for table in tables:
            iteminfo.append(table.parent)

        for item in iteminfo:
            print(item.find(class_='title').getText()) #이름
            print(item.find('a')['href']) #링크
            print(item.find('strong').getText()) #가격
            print(item.find('img')['src']) #이미지


temp = Gmarket("http://search.gmarket.co.kr/search.aspx?selecturl=total&sheaderkey=&gdlc=&SearchClassFormWord=goodsSearch&keywordOrg=%A4%B1&keywordCVT=%B9%CC%BC%BC%B8%D5%C1%F6%B8%B6%BD%BA%C5%A9%2C%B8%B6%BD%BA%C5%A9%2C%B9%B0%C6%BC%BD%B4%2C%B8%F0%C0%DA%2C%B8%C7%C5%F5%B8%C7%2C%B8%F0%B4%CF%C5%CD%2C%B9%CD%BC%AD%B1%E2%2C%C0%FC%B1%E2+%B8%E9%B5%B5%B1%E2%2C%B9%AE%C8%AD%BB%F3%C7%B0%B1%C7%2C%B8%B6%BF%EC%BD%BA&keywordCVTi=1&keyword=%B8%E9%B5%B5%B1%E2")
temp.item_info()

