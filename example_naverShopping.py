from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://search.shopping.naver.com/search/all.nhn?query=%EB%A9%B4%EB%8F%84%EA%B8%B0&cat_id=&frm=NVSHATC/" # 사용한 예시 url, 네이버 쇼핑(면도기)
html = urlopen(url)
source = html.read() # 바이트코드 type으로 소스를 읽는다.
html.close() # urlopen을 진행한 후에는 close를 한다.

soup = BeautifulSoup(source, "html.parser") # 사용한 라이브러리는 html.parser를 이용 (적당한 속도, 적당한 관대함)
table = soup.find(class_="sort_content") # 웹에 보여지는 제품군들의 집합
items = table.find_all(class_="ad _itemSection") # 각각의 제품을 리스트로 형성
for item in items : # 형성된 리스트를 반복문을 통해 하나씩 불러 읽음
    info = item.find(class_="info") # 제품에 대한 정보는 info class에 존재하므로 find를 통해 해당 클래스의 정보를 읽음
    title = info.find(class_="tit").get('title') # 제품명은 class tit 에 title이란 속성으로 존재하므로 이를 읽음
    price = info.find(class_="num _price_reload").get_text()
    '''
    제품 가격은 span class num _price_reload에 존재하지만 클래스 내부 속성에 존재하는 것이 아닌 자식과도 같은 위치에 존재
    따라서 get_text()를 통해 값을 읽음
    '''
    print(str(title) + " " + str(price))