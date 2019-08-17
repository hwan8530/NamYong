from bs4 import BeautifulSoup

from Crawling import Crawling
from Product_Info import Product_Info


class Auction(Crawling):
    def __init__(self, url):
        super().__init__(url)

    def getSoup(self, source):
        return BeautifulSoup(source, "html.parser")

    def setTable(self):
        return self.soup.find(id="section--inner_content_body_container")

    def setItems(self, table):
        return table.find_all(class_="component component--item_card type--general component--item_card_for_design")

    def printAllItems(self):
        table = self.soup.find(id="section--inner_content_body_container")
        items = table.find_all(class_="section--itemcard")
        for item in items :
            link = item.find("a").attrs['href']
            title = item.find(class_="text--title").getText()
            price = item.find(class_="text--price_seller").getText()
            print("제품명 : " + title + " 가격 : " + price)
            print(" 링크 : " + link)
        #image tag can't lead because they use lazyload

    def printChanceItems(self):
        table = self.soup.find(class_="component component--chance_shopping")
        items = table.find_all(class_="item")

        for item in items :
            if item != None :
             link = item.find("a").attrs['href']
             title = item.find("img").attrs['alt']
             image = item.find("img").attrs['src']
             price = item.find(class_="text--price_number").getText()
             print("제품명 : " + title + " 가격 : "+price)
             print("image : "+image + " 링크 : "+link)

ac = Auction("http://browse.auction.co.kr/search?keyword=%EB%A9%B4%EB%8F%84%EA%B8%B0&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=%EB%A9%B4%EB%8F%84%EA%B8%B0&acode=SRP_SU_0100&arraycategory=&encKeyword=%EB%A9%B4%EB%8F%84%EA%B8%B0")
print(ac.soup)