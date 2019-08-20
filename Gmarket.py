from bs4 import BeautifulSoup
from Crawling import *
from selenium.webdriver.common.keys import Keys
class Gmarket(Crawling):
    def __init__(self, url):
        super().__init__()
        self.setUrl(url)
        self.getHtml()
        self.parseSoup()

    def setUrl(self, newUrl):
        self.url = newUrl
        self.driver.get(self.url)

    def all_Item(self):
        return self.soup.find_all(class_="item_info")

    def item_info(self):
        tables = (self.soup.find_all(class_ = "item_info"))
        iteminfo = []

        for table in tables:
            iteminfo.append(table.parent)

        for item in iteminfo:
            print(item.find(class_='title').getText()) #이름
            print(item.find('a')['href']) #링크
            print(item.find('strong').getText()) #가격
            print(item.find('img')['src']) #이미지

    def nextPage(self):
        temp = self.driver.find_element_by_xpath('//*[@id="divListAjaxContainer"]/div[3]/span[4]/a')
        self.driver.execute_script('arguments[0].click();', temp)
        self.getHtml()
        self.parseSoup()
        # self.driver.execute_script("argument[0].click();", cli)
        # nextButtonSession = nextButtonSession.find_element_by_tag_name('a')
        # nextButtonSession.click()
        print("gdgdgdgdgdgdgdgdgdgdgd")
        # self.item_info()

# temp = Gmarket("http://search.gmarket.co.kr/search.aspx?selecturl=total&sheaderkey=&gdlc=&SearchClassFormWord=goodsSearch&keywordOrg=%A4%B1&keywordCVT=%B9%CC%BC%BC%B8%D5%C1%F6%B8%B6%BD%BA%C5%A9%2C%B8%B6%BD%BA%C5%A9%2C%B9%B0%C6%BC%BD%B4%2C%B8%F0%C0%DA%2C%B8%C7%C5%F5%B8%C7%2C%B8%F0%B4%CF%C5%CD%2C%B9%CD%BC%AD%B1%E2%2C%C0%FC%B1%E2+%B8%E9%B5%B5%B1%E2%2C%B9%AE%C8%AD%BB%F3%C7%B0%B1%C7%2C%B8%B6%BF%EC%BD%BA&keywordCVTi=1&keyword=%B8%E9%B5%B5%B1%E2")
temp = Gmarket("http://search.gmarket.co.kr/search.aspx?selecturl=total&sheaderkey=&gdlc=&SearchClassFormWord=goodsSearch&keywordOrg=%B9%D9%B5%F0%BF%EC&keywordCVT=%B9%D9%B5%F0%BF%F6%BD%C3%2C%C7%D8%C7%C7%B9%D9%BD%BA+%B9%D9%B5%F0%BF%F6%BD%C3%2C%BF%C2%B4%F5%B9%D9%B5%F0+%B9%D9%B5%F0%BF%F6%BD%C3&keywordCVTi=1&keyword=%B9%D9%B5%F0%BF%F6%BD%C3")
temp.item_info()
temp.nextPage()
# temp.driver.quit()


