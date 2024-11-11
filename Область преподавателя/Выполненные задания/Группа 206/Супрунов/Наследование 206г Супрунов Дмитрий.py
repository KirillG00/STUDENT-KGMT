class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"{self.name} is {self.age} years old."

class Dog(Animal):
    def bark(self):
        return "Woof! Woof!"

class Cat(Animal):
    def meow(self):
        return "Meow!"

class Bird(Animal):
    def chirp(self):
        return "Chirp! Chirp!"

dog = Dog(name="Buddy", age=3)
cat = Cat(name="Whiskers", age=2)
bird = Bird(name="Tweety", age=1)

print(dog.info())
print(dog.bark())

print(cat.info())
print(cat.meow())

print(bird.info())
print(bird.chirp())

input()