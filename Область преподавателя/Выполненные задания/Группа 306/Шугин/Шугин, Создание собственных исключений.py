# Исключение для некорректного имени
class InvalidNameError(Exception):
    pass

# Исключение для некорректного возраста
class InvalidAgeError(Exception):
    pass

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def set_name(self, name):
        if not name.isalpha():
            raise InvalidNameError("Имя должно состоять только из букв.")
        self.name = name

    def set_age(self, age):
        if not age.isdigit() or int(age) <= 0:
            raise InvalidAgeError("Возраст должен состоять из цифр и быть больше нуля.")
        self.age = int(age)

# Пример использования
def create_animal():
    try:
        name = input("Введите имя животного: ")
        age = input("Введите возраст животного: ")
        animal = Animal(name, age)
        print(f"Животное создано: {animal.name}, возраст: {animal.age}")
    except (InvalidNameError, InvalidAgeError) as e:
        print(f"Ошибка: {e}")

# Запуск функции для создания животного
create_animal()

input()