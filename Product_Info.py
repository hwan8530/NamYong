class Product_Info:
    # 제품정보 instance
    def __init__(self, name, price, image, url):
        self.__name = name
        self.__price = price
        self.__image = image
        self.__url = url

    # getter & setter
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, newPrice):
        self.__price = newPrice

    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, newImage):
        self.__image = newImage

    @property
    def url(self):
        return self.__url
    @url.setter
    def url(self, newURL):
        self.__url = newURL


