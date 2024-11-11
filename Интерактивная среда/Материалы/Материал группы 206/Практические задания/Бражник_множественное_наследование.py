
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        return self.sound
    def info(self):
        return f"Name: {self.name}, Sound: {self.sound}"
class Mammal(Animal):
    def __init__(self, name, sound, fur_color):
        super().__init__(name, sound)
        self.fur_color = fur_color
    def info(self):
        return f"{super().info()}, Fur Color: {self.fur_color}"
class Bird(Animal):
    def __init__(self, name, sound, wingspan):
        super().__init__(name, sound)
        self.wingspan = wingspan
    def info(self):
        return f"{super().info()}, Wingspan: {self.wingspan} cm"
class MarineAnimal(Animal):
    def __init__(self, name, sound, depth):
        super().__init__(name, sound)
        self.depth = depth
    def info(self):
        return f"{super().info()}, Max Depth: {self.depth} m"
class Pet:
    def fetch(self):
        return f"{self.name} is fetching the ball!"
class NoFlyBird:
    def do_not_fly(self):
        return f"{self.name} cannot fly."
class Fish:
    def swim(self):
        return f"{self.name} is swimming!"
class Dog(Mammal, Pet):
    def __init__(self, name, sound, fur_color):
        super().__init__(name, sound, fur_color)
class Penguin(Bird, Fish):
    def __init__(self, name, sound, wingspan):
        super().__init__(name, sound, wingspan)
    def do_not_fly(self):
        return f"{self.name} is a penguin and cannot fly."
class Dolphin(MarineAnimal, Fish):
    def __init__(self, name, sound, depth):
        super().__init__(name, sound, depth)
dog = Dog(name="Buddy", sound="Woof!", fur_color="Brown")
penguin = Penguin(name="Pingu", sound="Honk!", wingspan=80)
dolphin = Dolphin(name="Flipper", sound="Click!", depth=300)

print(dog.info())
print(dog.make_sound())
print(dog.fetch())

print(penguin.info())
print(penguin.make_sound())
print(penguin.swim())
print(penguin.do_not_fly())

print(dolphin.info())
print(dolphin.make_sound())
print(dolphin.swim())