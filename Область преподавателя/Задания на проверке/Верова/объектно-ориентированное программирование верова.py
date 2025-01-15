class Rectangle:

    def __init__(self, a, b):
        self.width = a
        self.length = b

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)


rect1 = Rectangle(40, 40)
print("rect1 area: ", rect1.area())
print("rect1 perimeter: ", rect1.perimeter())

rect2 = Rectangle(20, 30)
print("rect2 area: ", rect2.area())
print("rect2 perimeter: ", rect2.perimeter())