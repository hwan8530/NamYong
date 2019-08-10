from asynchat import async_chat

from Crawling import *

class Auction(Crawling) :
    def __init__(self, url):
        super().__init__(url)

    def getSoup(self, source):
        return BeautifulSoup(source,"html.parser")

    def setTable(self):
        return self.soup.find(id="section--inner_content_body_container")

    def setItems(self, table):
        return table.find_all(class_="section--module_wrap")

    def printAllItems(self):
        table = self.setTable();
        items = self.setItems(table);

        for item in items :
            if item != None:
                info = item.find(class_="section--item_information")
                title = info.find(class_="link--description_1").getText();
                price = info.find(class_="text--price_number")
                print(title+" "+price)


ac = Auction("http://browse.auction.co.kr/search?keyword=%EB%A9%B4%EB%8F%84%EA%B8%B0&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=%EB%A9%B4%EB%8F%84%EA%B8%B0&acode=SRP_SU_0100&arraycategory=&encKeyword=%EB%A9%B4%EB%8F%84%EA%B8%B0")
ac.printAllItems()