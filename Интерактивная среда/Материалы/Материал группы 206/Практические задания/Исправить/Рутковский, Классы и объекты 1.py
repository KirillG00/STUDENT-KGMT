class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

        def area(self):
            return self.width * self.length

        def perimeter(self):
            return 2 * (self.width +
self.length)


rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(3, 7)
print(f"Площадь прямоугольника 1:
{rectangle1.area()}") #Неверно происходит вывод!

print(f"Площадь прямоугольника 1:
{rectangle1.perimeter()}") #Неверно происходит вывод!

print(f"Площадь прямоугольника 2:
{rectangle2.area()}") #Неверно происходит вывод!

print(f"Площадь прямоугольника 2:
{rectangle2.perimeter()}") #Неверно происходит вывод!

input()