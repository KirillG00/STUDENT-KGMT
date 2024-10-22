class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        """Возвращает площадь прямоугольника."""
        return self.width * self.length

    def perimeter(self):
        """Возвращает периметр прямоугольника."""
        return 2 * (self.width + self.length)
if __name__ == "__main__":
    rect = Rectangle(5, 10)
    print("Ширина:", rect.width)
    print("Длина:", rect.length)
    print("Площадь:", rect.area())
    print("Периметр:", rect.perimeter())