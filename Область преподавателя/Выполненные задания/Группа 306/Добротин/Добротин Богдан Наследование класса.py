class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

class Dog(Animal):
    def bark(self):
        return "Гав-гав!"

class Cat(Animal):
    def meow(self):
        return "Мяу!"

class Bird(Animal):
    def sing(self):
        return "Чирик-чирик!"

dog = Dog("Рекс", 3)
cat = Cat("Мурка", 2)
bird = Bird("Чижик", 1)


print(dog.get_info())
print(dog.bark())

print(cat.get_info())
print(cat.meow())

print(bird.get_info())
print(bird.sing())

input()