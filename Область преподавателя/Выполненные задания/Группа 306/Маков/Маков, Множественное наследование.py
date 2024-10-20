class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return self.sound

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
        return "Fetching!"

class NoFlyBird:
    def do_not_fly(self):
        return "I can't fly!"

class Fish:
    def swim(self):
        return "Swimming!"

class Dog(Mammal, Pet):
    def info(self):
        return f"{self.name} makes {self.make_sound()} sound and has {self.fur_color} fur."

class Penguin(Bird, Fish, NoFlyBird):
    def info(self):
        return f"{self.name} makes {self.make_sound()} sound and has a wingspan of {self.wingspan}."

class Dolphin(MarineAnimal, Fish):
    def info(self):
        return f"{self.name} makes {self.make_sound()} sound and can dive to {self.depth} meters."

# Создание экземпляров
dog = Dog("Buddy", "Bark", "Brown")
penguin = Penguin("Pingu", "Honk", "1.2m")
dolphin = Dolphin("Flipper", "Click", 300)

# Вызов методов
print(dog.info())        # Информация о собаке
print(penguin.info())    # Информация о пингвине
print(dolphin.info())     # Информация о дельфине
input()