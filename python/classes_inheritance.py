# Inheritance
class SUPERCLASS():
    def spam(self):
        print(1)


class SUBCLASS(SUPERCLASS):
    def spam(self):
        super().spam()  # inherited from superclass
        print(2)


csup = SUPERCLASS()
csup.spam()
csub = SUBCLASS()
csub.spam()
