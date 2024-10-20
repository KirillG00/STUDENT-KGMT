class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return self.sound

    def info(self):
        return f"Animal: {self.name}, Sound: {self.sound}"


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
        Mammal.__init__(self, name, sound, fur_color)


class Penguin(Bird, Fish, NoFlyBird):
    def __init__(self, name, sound, wingspan):
        Bird.__init__(self, name, sound, wingspan)


class Dolphin(MarineAnimal, Fish):
    def __init__(self, name, sound, depth):
        MarineAnimal.__init__(self, name, sound, depth)


# Создание экземпляров классов
dog = Dog(name="Buddy", sound="Woof!", fur_color="Brown")
penguin = Penguin(name="Pingu", sound="Squawk!", wingspan=90)
dolphin = Dolphin(name="Dolly", sound="Click!", depth=300)

# Вызов методов
print(dog.make_sound())  # Вывод: Woof!
print(dog.fetch())  # Вывод: Buddy is fetching the ball!
print(dog.info())  # Вывод: Animal: Buddy, Sound: Woof!, Fur Color: Brown

print(penguin.make_sound())  # Вывод: Squawk!
print(penguin.swim())  # Вывод: Pingu is swimming!
print(penguin.do_not_fly())  # Вывод: Pingu cannot fly.
print(penguin.info())  # Вывод: Animal: Pingu, Sound: Squawk!, Wingspan: 90 cm

print(dolphin.make_sound())  # Вывод: Click!
print(dolphin.swim())  # Вывод: Dolly is swimming!
print(dolphin.info())  # Вывод: Animal: Dolly, Sound: Click!, Max Depth: 300 m

input()