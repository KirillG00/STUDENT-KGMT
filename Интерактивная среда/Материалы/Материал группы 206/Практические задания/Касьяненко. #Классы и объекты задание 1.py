#Классы и объекты задание 1
class Rectangle:
    def __init__(self, width, length):
        self.width = width  # Атрибут ширины
        self.length = length  # Атрибут длины

    def area(self):
        """Метод для вычисления площади прямоугольника."""
        return self.width * self.length

    def perimeter(self):
        """Метод для вычисления периметра прямоугольника."""
        return 2 * (self.width + self.length)

# Пример использования класса Rectangle
rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(3, 7)

print(f"Площадь прямоугольника 1: {rectangle1.area()}")  # Вывод: 50
print(f"Периметр прямоугольника 1: {rectangle1.perimeter()}")  # Вывод: 30

print(f"Площадь прямоугольника 2: {rectangle2.area()}")  # Вывод: 21
print(f"Периметр прямоугольника 2: {rectangle2.perimeter()}")  # Вывод: 20