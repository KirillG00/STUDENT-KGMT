class AnimalError(Exception):
    """Базовый класс для исключений, связанных с животными."""
    pass

class InvalidNameError(AnimalError):
    """Исключение для неверного имени животного."""
    def __init__(self, name):
        super().__init__(f"Имя '{name}' не должно содержать цифры.")
        input()
class InvalidAgeError(AnimalError):
    """Исключение для неверного возраста животного."""
    def __init__(self, age):
        super().__init__(f"Возраст '{age}' должен быть числом больше нуля.")
        input() 

class Animal:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def set_name(self, name):
        if any(char.isdigit() for char in name):
            raise InvalidNameError(name)
        self.name = name

    def set_age(self, age):
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(age)
        self.age = age

def main():
    name = input("Введите имя животного: ")
    age = int(input("Введите возраст животного: "))
    input()

    try:
        animal = Animal(name, age)
        print(f"Животное создано: {animal.name}, {animal.age} лет.")
        input()

    except AnimalError as e:
        print(e)
        input()

if __name__ == "__main__":
    main()
    input()