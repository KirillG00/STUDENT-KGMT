class AnimalError(Exception):
    """Базовый класс для исключений, связанных с животными."""
    pass

class InvalidNameError(AnimalError):
    """Исключение для неправильного имени животного."""
    def __init__(self, name):
        self.name = name
        super().__init__(f"Имя '{name}' не должно содержать цифр.")

class InvalidAgeError(AnimalError):
    """Исключение для неправильного возраста животного."""
    def __init__(self, age):
        self.age = age
        super().__init__(f"Возраст '{age}' должен быть больше 0 и состоять только из цифр.")

class Animal:
    def __init__(self, name, age):
        if any(char.isdigit() for char in name):
            raise InvalidNameError(name)
        self.name = name

        if not age.isdigit() or int(age) <= 0:
            raise InvalidAgeError(age)
        self.age = int(age)

# Ввод данных от пользователя
try:
    name = input("Введите имя животного: ")
    age = input("Введите возраст животного: ")
    animal = Animal(name, age)
    print(f"Создано животное: {animal.name}, возраст: {animal.age}")
except AnimalError as e:
    print(e)