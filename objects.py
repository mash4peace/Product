class Product:
    def __init__(self, name = '', price =  0.0 , discountPercent = 0):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent


    def getDiscountAmount(self):
        return self.price * self.discountPercent/100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getDiscription(self):
        return self.name


class Book(Product):
    def __init__(self, name = '', price = 0.0, disciuntPercent = 0, author = ''):
        Product.__init__(self, name, price, disciuntPercent)
        self.author = author

    def getDescription(self):
        return Product.getDiscription(self) + " by"+ self.author


class Movie(Product):
    def __init__(self, name = '', price = 0.0, discountPercent = 0 , year = 0):
        Product.__init__(self, name , price, discountPercent)
        self.year = year

    def getDiscription(self):
        return Product.getDiscription(self) + " (" + str(self.year) + ")"


