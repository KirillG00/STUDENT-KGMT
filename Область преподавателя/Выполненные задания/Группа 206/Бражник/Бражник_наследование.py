class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return f"{self.name} is {self.age} years old"
class Dog(Animal):
    def bark(self):
        return"woof"
class Cat(Animal):
    def meow(self):
        return"meow"
class Bird(Animal):
    def chirik(self):
        return "chirik"

dog = Dog("buddy",3)
cat = Cat("kitten",2)
bird = Bird("smoll bird",1)

print(dog.info())
print(dog.bark())
print(cat.info())
print(cat.meow())
print(bird.info())
print(bird.chirik())

input()