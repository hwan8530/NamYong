from bs4 import BeautifulSoup
from time import sleep
from Crawling import Crawling
from Product_Info import Product_Info

class Auction(Crawling):
    images = []
    productList = []
    pageNum = 1
    def __init__(self, url):
        super().__init__(url)
        self.setUrl(url)

    def waitForLoad(self):
        #self.driver.implicitly_wait(3)
        elements = []
        for i in range(15):
            sleep(0.5)
            self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight/(15))")
            elements = self.driver.find_elements_by_class_name("image--itemcard  ")
            sleep(0.5)

        for element in elements:
            self.images.append(element.get_attribute("src"))

    def setUrl(self, url):
        self.pageNum = 1
        self.driver.get(url)
        self.getHtml()
        self.parseSoup()
        self.images = []
        self.waitForLoad()

    def closeDriver(self):
        self.driver.quit()

    def setAllItems(self):
        table = self.soup.find(id="section--inner_content_body_container")
        items = table.find_all(class_="section--itemcard")
        cnt = 0
        for item in items :
            link = item.find("a").attrs['href']
            title = item.find(class_="text--title").getText()
            price = item.find(class_="text--price_seller").getText()
            self.productList.append(Product_Info(title,price,self.images[cnt],link))
            cnt = cnt + 1

    def setChanceItems(self):
        table = self.soup.find(class_="component component--chance_shopping")
        items = table.find_all(class_="item")

        for item in items :
            if item != None :
             link = item.find("a").attrs['href']
             title = item.find("img").attrs['alt']
             image = item.find("img").attrs['src']
             price = item.find(class_="text--price_number").getText()
             self.productList.append(Product_Info(title,price,image,link))

    def printProductlist(self):
        for product in self.productList:
            print("제품 : "+product.name+" 가격 : "+product.price)
            print("img : "+product.image+" 링크 : "+product.url)

    def setNextPage(self, url):
        newUrl = url[0:len(url)-1]
        self.pageNum = self.pageNum+1
        newUrl+=str(self.pageNum)
        self.setUrl(newUrl)
        self.setAllItems()

    def getNextPageItem(self):
        self.setNextPage(self.driver.current_url)
        self.setAllItems()


ac = Auction("http://browse.auction.co.kr/search?keyword=%ec%83%b4%ed%91%b8&itemno=&nickname=&encKeyword=%25EC%2583%25B4%25ED%2591%25B8&arraycategory=&frm=&dom=auction&isSuggestion=No&retry=&k=32&p=1")
ac.setChanceItems()
ac.setAllItems()
ac.printProductlist()
ac.getNextPageItem()
ac.printProductlist()