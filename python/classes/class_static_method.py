# @classmethod more then one constructor
# @staticmethod Static methods behave like plain functions,
#    except for the fact that you can call them from an instance of the class.


class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return (self.width * self.height)

    @classmethod
    def new_squere(cls, side_length):
        return cls(side_length, side_length)


square = Rectangle.new_squere(5)
print(square.calculate_area())


# @staticmethod
class Pizza():
    def __init__(self, topping):
        self.topping = topping

    @staticmethod
    def validate_topping(topping):
        if topping == "pinapple":
            raise ValueError("No pineapples!")
        else:
            return True


ingredients = ["chees", "tomato", "garlic"]
if all(Pizza.validate_topping(i) for i in ingrediaents):
    pizza = Pizza(ingrediaents)
