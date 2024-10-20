class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} makes a sound: {self.sound}")


class Mammal(Animal):
    def __init__(self, name, sound, fur_color):
        super().__init__(name, sound)
        self.fur_color = fur_color


class Bird(Animal):
    def __init__(self, name, sound, wingspan):
        super().__init__(name, sound)
        self.wingspan = wingspan


class MarineAnimal(Animal):
    def __init__(self, name, sound, depth):
        super().__init__(name, sound)
        self.depth = depth


class Pet:
    def fetch(self):
        print("This pet likes to play fetch.")


class NoFlyBird:
    def do_not_fly(self):
        print("This bird does not fly.")


class Fish:
    def swim(self):
        print("This fish is swimming.")


class Dog(Mammal, Pet):
    def info(self):
        print(f"Name: {self.name}\nSound: {self.sound}\nFur Color: {self.fur_color}")


class Penguin(Bird, Fish):
    def info(self):
        print(f"Name: {self.name}\nSound: {self.sound}\nWingspan: {self.wingspan}")


class Dolphin(MarineAnimal, Fish):
    def info(self):
        print(f"Name: {self.name}\nSound: {self.sound}\nDepth: {self.depth}")


dog = Dog("Rex", "Woof", "Brown")
penguin = Penguin("Pingo", "Honk", "Short")
dolphin = Dolphin("Dolly", "Click", 200)

input()


dog.info()
penguin.info()
dolphin.info()

input()