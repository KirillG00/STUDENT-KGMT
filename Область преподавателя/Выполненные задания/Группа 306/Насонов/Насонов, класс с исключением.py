class AnimalError(Exception):
    pass
class NameError(AnimalError):
    pass
class AgeError(AnimalError):
    pass
class Animal:
    def __init__(self, name, age):
        self.s_name(name)
        self.s_age(age)
    def s_name(self, name):
        if not name.isalpha():
            raise NameError("Имя животного не должно содержать цифры.(｡•́︿•̀｡)")
        self.name = name
    def s_age(self, age):
        if not age.isdigit() or int(age) <= 0:
            raise AgeError("Возраст должен быть положительным числом.╭∩╮( •̀_•́ )╭∩╮")
        self.age = int(age)

    def __str__(self):
        return f"Животное: {self.name}, Возраст: {self.age} лет ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧"
def Baza():
    try:
        name = input("Введите имя животного: ")
        age = input("Введите возраст животного: ")
        animal = Animal(name, age)
        print(animal)
    except AnimalError as e:
        print(f"Ошибочка: {e}")

if __name__ == "__main__":
    Baza()
input()