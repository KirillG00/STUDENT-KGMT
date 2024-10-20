class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class Animal:
    def __init__(self, name, age):
        if any(char.isdigit() for char in name):
            raise InvalidNameError("Имя не должно содержать цифр")
        self.name = name
        print("Имя: ", name)

        if not age.isdigit() or int(age) <= 0:
            raise InvalidAgeError("Возраст должен быть положительным, состоять из цифр и быть целым")
        self.age = int(age)
        print("Возраст: ", age)


try:
    name = input("Введите имя животного: ")
    age = input("Введите возраст животного: ")
    animal = Animal(name, age)
except InvalidNameError as e:
    print(e)
except InvalidAgeError as e:
    print(e)

input()