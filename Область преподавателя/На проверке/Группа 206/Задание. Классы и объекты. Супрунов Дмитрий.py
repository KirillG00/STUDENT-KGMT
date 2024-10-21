class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 4)

print(f"Прямоугольник 1: Площадь = {rect1.area()}, Периметр = {rect1.perimeter()}")
print(f"Прямоугольник 1: Площадь = {rect2.area()}, Периметр = {rect2.perimeter()}")