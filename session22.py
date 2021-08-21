class product:
    def __init__(self, name, brand , price):
        self.name = name
        self._brand = brand
        self.__price = price

    def __showproduct(self):
        print("product details are {}|{}|{}".format(self.name, self._brand, self.__price))

    def __str__(self):
        return "{} | {} | {}".format(self.name, self._brand, self.__price)

def main():
    pref = product("iPhone", "Apple", 60000)
    #pref.__showproduct()
    print(product.__dict__)

    print(pref)

if __name__ == '__main__':
    main()