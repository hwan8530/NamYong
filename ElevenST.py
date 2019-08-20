from selenium import webdriver
from bs4 import BeautifulSoup
from Crawling import Crawling


class elevenSt(Crawling):
    def __init__(self, url):
       super().__init__(url)

    def printRecommendedItems(self):
        table = self.soup.find("ul", class_="cfix")
        items = table.find_all(class_="box_pd")
        for item in items :
            #a = item.find("a")
            link = item.find("a").attrs['href']
            title = item.find("p").getText()
            price = item.find(class_="sale_price").getText()
            img = self.driver.find_element_by_class_name('lazy')

            print(title+" "+price)
            print(img+" "+link)


test = elevenSt("http://search.11st.co.kr/Search.tmall?kwd=%25EB%25A9%25B4%25EB%258F%2584%25EA%25B8%25B0")
test.printRecommendedItems()