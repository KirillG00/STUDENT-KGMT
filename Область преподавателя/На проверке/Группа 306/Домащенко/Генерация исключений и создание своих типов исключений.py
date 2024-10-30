class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def get_age(self):
        return self.age

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Имя должно быть строкой.")
        if any(char.isdigit() for char in new_name):
            raise NameError("Имя не должно содержать цифры.")
        self.name = new_name

    def set_species(self, new_species):
        if not isinstance(new_species, str):
            raise TypeError("Вид должен быть строкой.")
        self.species = new_species

    def set_age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError("Возраст должен быть целым числом.")
        if new_age <= 0:
            raise ValueError("Возраст должен быть больше нуля.")
        self.age = new_age

class InvalidNameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class InvalidSpeciesError(Exception):
    pass

while True:
    try:
        name = input("Введите имя животного: ")
        species = input("Введите вид животного: ")
        age = int(input("Введите возраст животного: "))
        animal = Animal(name, species, age)
        break
    except ValueError as e:
        print(f"Ошибка ввода возраста: {e}")
    except TypeError as e:
        print(f"Ошибка ввода имени или вида: {e}")
    except InvalidNameError as e:
        print(f"Ошибка: {e}")
    except InvalidAgeError as e:
        print(f"Ошибка: {e}")
    except InvalidSpeciesError as e:
        print(f"Ошибка: {e}")

print(f"Создано животное: имя: {animal.get_name()} вид: {animal.get_species()}, возраст: {animal.get_age()}")

input()