class NameError(Exception):
    pass

class AgeError(Exception):
    pass

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create(cls):
        name = input("Введите имя животного: ")
        age_input = input("Введите возраст животного: ")

        if any(char.isdigit() for char in name):
            raise NameError("Имя не должно содержать цифр.")

        try:
            age = float(age_input)
            if age <= 0:
                raise AgeError("Возраст должен быть больше нуля.")
        except ValueError:
            raise AgeError("Возраст должен состоять только из цифр.")

        return cls(name, age)

    def __str__(self):
        return f"Животное: {self.name}, Возраст: {self.age} лет"

if __name__ == '__main__':
    try:
        animal = Animal.create()
        print(animal)
    except (NameError, AgeError) as e:
        print(f"Ошибка: {e}")

input()