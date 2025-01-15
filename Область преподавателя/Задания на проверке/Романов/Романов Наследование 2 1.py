class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        """Метод для получения информации о животном."""
        return f"{self.name} is {self.age} years old."

class Dog(Animal):
    def bark(self):
        """Метод, который заставляет собаку лаять."""
        return f"{self.name} says Woof!"
class Cat(Animal):
    def meow(self):
        """Метод, который заставляет кошку мяукать."""
        return f"{self.name} says Meow!"
class Bird(Animal):
    def chirp(self):
        """Метод, который заставляет птицу чирикать."""
        return f"{self.name} says Chirp!"
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)
bird = Bird("Tweety", 1)
print(dog.info())
print(dog.bark())
print(cat.info())
print(cat.meow())
print(bird.info())
print(bird.chirp())
