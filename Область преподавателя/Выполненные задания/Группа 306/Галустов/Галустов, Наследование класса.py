class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"{self.name} is {self.age} years old."


class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def meow(self):
        return f"{self.name} says Meow!"


class Bird(Animal):
    def chirp(self):
        return f"{self.name} says Chirp!"


# Создание объектов различных классов
dog = Dog("Buddy", 4)
cat = Cat("Whiskers", 3)
bird = Bird("Tweety", 1)

# Использование методов
print(dog.info())    # Вывод информации о собаке
print(dog.bark())    # Существует метод лая

print(cat.info())    # Вывод информации о кошке
print(cat.meow())    # Существует метод мяуканья

print(bird.info())   # Вывод информации о птице
print(bird.chirp())  # Существует метод чириканья

input()