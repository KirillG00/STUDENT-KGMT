class AnimalException(Exception):
    """Базовый класс исключений для животных"""
    pass

class NameErrorException(AnimalException):
    """Исключение, когда имя животного содержит цифры"""
    def __init__(self, name):
        self.message = f"В имени не должно быть цифр: {name}"
        super().__init__(self.message)

class AgeErrorException(AnimalException):
    """Исключение, когда возраст не является положительным числом"""
    def __init__(self, age):
        self.message = f"Возраст должен состоять из цифр и быть больше нуля: {age}"
        super().__init__(self.message)

class Animal:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def set_name(self, name):
        if any(char.isdigit() for char in name):
            raise NameErrorException(name)
        self.name = name

    def set_age(self, age):
        if not age.isdigit() or int(age) <= 0:
            raise AgeErrorException(age)
        self.age = int(age)

    def __str__(self):
        return f"Животное: {self.name}, Возраст: {self.age} лет"

def main():
    try:
        name = input("Введите имя животного: ")
        age = input("Введите возраст животного: ")
        animal = Animal(name, age)
        print(animal)
    except AnimalException as e:
        print(e)

if __name__ == "__main__":
    main()
    
input()