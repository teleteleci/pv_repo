class Spam():
    __egg = 7

    def printEgg(self):
        print("{0}".format(self.__egg))


s = Spam()
s.printEgg()
try:
    print(s.__egg)
except AttributeError:
    print("Can not acces to hidden attribute")
    print("_Spam__egg show/modify attribute value: {0}".format(s._Spam__egg))
