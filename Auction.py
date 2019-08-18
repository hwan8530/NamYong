from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from Crawling import Crawling
from Product_Info import Product_Info


class Auction(Crawling):
    def __init__(self, url):
        super().__init__(url)
        self.waitForLoad()
        self.getHtml()
        self.parseSoup()
        self.driver.quit()
    def waitForLoad(self):
        self.driver.implicitly_wait(3)
        temp = 0
        for i in range(10):
            sleep(1)
            self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight/(10))")
            sleep(1)
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #try:
            #element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "image--itemcard")))

        #finally:
            #self.driver.quit()

    def printAllItems(self):
        table = self.soup.find(id="section--inner_content_body_container")
        items = table.find_all(class_="section--itemcard")
        for item in items :
            link = item.find("a").attrs['href']
            img = item.find("img").attrs['src']
            print(img)
            title = item.find(class_="text--title").getText()
            price = item.find(class_="text--price_seller").getText()
            print("제품명 : " + title + " 가격 : " + price)
            print(" 링크 : " + link+ " 이미지 : "+img)
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
ac.printAllItems()