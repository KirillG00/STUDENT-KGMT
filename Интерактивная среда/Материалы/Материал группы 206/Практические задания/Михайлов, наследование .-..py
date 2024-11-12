class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
            return f"Name: {self.name}, Age {self.age}"

class Dog(Animal):
    def bark(self):
        return "Woof!"

class Cat(Animal):
    def meow(self):
        return "Meow!"

class Bird(Animal):
    def chirp(self):
        return "Chirp!"

dog = Dog(name="Rex", age=5)
cat = Cat(name="Wittens", age=3)
bird = Bird(name="Tweety", age=2)

print(dog.info())
print(dog.bark())

print(cat.info())
print(cat.meow())

print(bird.info())
print(bird.chirp())