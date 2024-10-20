class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def get_info(self):
        return f"Имя: {self.name}, Вид: {self.species}, Возраст: {self.age}"

    def __str__(self):
        return self.get_info()

class InvalidName(Exception):
    pass

class InvalidSpecies(Exception):
    pass

class InvalidAge(Exception):
    pass

def create_animal():
    while True:
        try:
            name = input("Введите имя животного: ")
            if not name.isalpha():
                raise InvalidName("Имя должно состоять только из букв.")

            species = input("Введите вид животного: ")
            if not species.isalpha():
                raise InvalidSpecies("Вид должен состоять только из букв.")

            age = int(input("Введите возраст животного: "))
            if age <= 0:
                raise InvalidAge("Возраст должен быть положительным числом.")

            return Animal(name, species, age)

        except InvalidName as e:
            print(e)
        except InvalidSpecies as e:
            print(e)
        except InvalidAge as e:
            print(e)
        except ValueError:
            print("Возраст должен быть целым числом.")

animal = create_animal()
print(f"Создано живОтНОЕ:", animal)

input()