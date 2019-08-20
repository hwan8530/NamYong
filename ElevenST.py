from Crawling import *

class ElevenST(Crawling):
    def __init__(self, url):
        super().__init__(url)
        self.getHtml()
        self.parseSoup()

    def item_info(self):
        all_item = self.driver.find_elements_by_class_name('total_listitem')

        # self.driver.
        for item in all_item:
            print(item.find_element_by_class_name('info_tit').text) #제품명
            print(item.find_element_by_class_name('sale_price').text) #가격
            print(((item.find_element_by_class_name('info_tit')).find_element_by_tag_name('a')).get_attribute('href')) #상품링크
            self.waitForLoad()
            print((item.find_element_by_class_name('lazy')).get_attribute('src'))

test = ElevenST('http://search.11st.co.kr/Search.tmall?kwd=%25EB%25A9%25B4%25EB%258F%2584%25EA%25B8%25B0')
test.item_info()