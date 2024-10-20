class Animal:
    def __init__(self, name, age):
        self.name = name  # Имя животного
        self.age = age    # Возраст животного

# Подкласс Dog
class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"

# Подкласс Cat
class Cat(Animal):
    def meow(self):
        return f"{self.name} says Meow!"

# Подкласс Bird
class Bird(Animal):
    def chirp(self):
        return f"{self.name} says Chirp!"


dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)
bird = Bird("Tweety", 1)


print(dog.bark())  # Вывод: Buddy says Woof!
print(cat.meow())  # Вывод: Whiskers says Meow!
print(bird.chirp())  # Вывод: Tweety says Chirp!
input()