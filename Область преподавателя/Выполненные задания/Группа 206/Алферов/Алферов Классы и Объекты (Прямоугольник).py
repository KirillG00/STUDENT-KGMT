class Rectangle:

    def __init__(self, width, length ):
            self.width = width
            self.length = length

    def area(self):
        return (self.width * self.length)

    def perimeter (self):
       return 2 * (self.width + self.length)

rect = Rectangle(10,20)

print(f"Rectangle: width = {rect.width}, length = {rect.length}")
print(f"Rectangle area: Area = {rect.area()}")
print (f"Rectangle perimeter: Perimetr = {rect.perimeter()}")

input()