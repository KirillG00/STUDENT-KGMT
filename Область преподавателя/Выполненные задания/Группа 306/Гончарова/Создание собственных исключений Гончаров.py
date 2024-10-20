class InvalidNameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class Animal:
    def __init__(self, name, age):
        if any(char.isdigit() for char in name):
            raise InvalidNameError("Имя должно состоять из букв")
        self.name = name

        if float(age) <= 0:
            raise InvalidAgeError("Возраст должен быть больше 0 и быть числом")
        self.age = float(age)

try:
    name = input("Введите имя животного: ")
    age = input("Введите возраст животного: ")
    animal = Animal(name, age)
    print(f"Животное с именем {animal.name} и возрастом {animal.age}")
except InvalidNameError as e:
    print(f"Ошибка: {e}")
except InvalidAgeError as e:
    print(f"Ошибка: {e}")

input()