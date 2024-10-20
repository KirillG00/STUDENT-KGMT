class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name(self):
        return self.name

    def display_info(self):
        print(f"Name: {self.name}")

    def age(self):
        return self.age

    def bisplay_info(self):
        print(f"Age: {self.age}")
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing")

dog = Dog("Sobachka", 3)
cat = Cat("Kotik", 2)
dog.display_info()
dog.bisplay_info()
dog.bark()

cat.display_info()
cat.bisplay_info()
cat.meow()