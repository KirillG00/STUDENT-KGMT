
class InvalidName(Exception):
    pass

class InvalidAge(Exception):
    pass

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        if not name.isalpha():
            raise InvalidName("Ошибка имени")
        if not age.isdigit() or int(age) <= 0:
            raise InvalidAge("Ошибка возвраста")

    def __str__(self):
        return f"Животное под именем {self.name} возраст  {self.age} "

def create_animal():
    name = input("Имя: ")
    age = input("Возвраст: ")

    try:
        animal = Animal(name, age)
        print(animal)
    except InvalidName as e:
        print(f"Error: {e}")
        print("Попробуйте снова")
        create_animal()
    except InvalidAge as e:
        print(f"Исключение: {e}")
        print("Попробуйте снова")
        create_animal()


create_animal()

input()