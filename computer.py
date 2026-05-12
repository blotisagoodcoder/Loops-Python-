class Holoputer: 
    def __init__(self):
        self.__maxprice = 12000
    def sell(self):
        print("YO THIS EXPENSIVE: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price

h = Holoputer()
h.sell()
h.__maxprice = 15000
h.sell()
h.setMaxPrice(15000)
h.sell()
