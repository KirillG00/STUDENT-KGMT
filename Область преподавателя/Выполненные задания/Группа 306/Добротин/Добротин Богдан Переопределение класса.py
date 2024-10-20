class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

    def make_sound(self):
        return "Звук животного"

class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"

    def bring_ball(self):
        return "Собака приносит мяч"

class Cat(Animal):
    def make_sound(self):
        return "Мяу!"

    def catching_mice(self):
        return "Кошка ловит мышей"

class Bird(Animal):
    def make_sound(self):
        return "Чирик-чирик!"

    def fly(self):
        return "Птица летит"

# Создаем объекты
dog = Dog("Рекс", 6)
cat = Cat("Мурка", 2)
bird = Bird("Чижик", 1)

# Вывод информации и демонстрация методов
print(dog.get_info())
print(dog.make_sound())
print(dog.bring_ball())

print(cat.get_info())
print(cat.make_sound())
print(cat.catching_mice())

print(bird.get_info())
print(bird.make_sound())
print(bird.fly())