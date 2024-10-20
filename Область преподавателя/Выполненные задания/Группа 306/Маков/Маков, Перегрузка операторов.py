class Vector:
    def __init__(self, x, y):
        """Инициализация вектора с координами x и y."""
        self.x = x
        self.y = y

    def __add__(self, other):
        """Оператор сложения векторов."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """Оператор вычитания векторов."""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __repr__(self):
        """Строковое представление вектора."""
        return f"Vector({self.x}, {self.y})"


# Пример использования:
v1 = Vector(1, 2)
v2 = Vector(3, 4)

sum_vector = v1 + v2  # Сложение векторов
difference_vector = v1 - v2  # Вычитание векторов

print("Сумма:", sum_vector)  # Вывод: Vector(4, 6)
print("Разность:", difference_vector)  # Вывод: Vector(-2, -2)

input()