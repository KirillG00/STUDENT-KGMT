class Animal:
    def __init__(self, name, sound):
        self.name = name  # Имя
        self.sound = sound  # Звук

    def make_sound(self):
        return f"{self.name} says {self.sound}"

    def info(self):
        return f"Name: {self.name}, Sound: {self.sound}"


class Mammal(Animal):
    def __init__(self, name, sound, fur_color):
        super().__init__(name, sound)
        self.fur_color = fur_color  # Цвет шерсти

    def info(self):
        return f"{super().info()}, Fur Color: {self.fur_color}"


class Bird(Animal):
    def __init__(self, name, sound, wingspan):
        super().__init__(name, sound)
        self.wingspan = wingspan  # Размах крыльев

    def info(self):
        return f"{super().info()}, Wingspan: {self.wingspan} cm"


class MarineAnimal(Animal):
    def __init__(self, name, sound, depth):
        super().__init__(name, sound)
        self.depth = depth  # Максимальная глубина погружения

    def info(self):
        return f"{super().info()}, Max Depth: {self.depth} meters"


class Pet:
    def fetch(self):
        return f"{self.name} is fetching the ball!"


class NoFlyBird:
    def do_not_fly(self):
        return f"{self.name} cannot fly."


class Fish:
    def swim(self):
        return f"{self.name} is swimming."


class Dog(Mammal, Pet):
    def __init__(self, name, sound, fur_color):
        Mammal.__init__(self, name, sound, fur_color)


class Penguin(Bird, Fish, NoFlyBird):
    def __init__(self, name, sound, wingspan):
        Bird.__init__(self, name, sound, wingspan)


class Dolphin(MarineAnimal, Fish):
    def __init__(self, name, sound, depth):
        MarineAnimal.__init__(self, name, sound, depth)


# Создание экземпляров
dog = Dog("Buddy", "Woof", "Brown")
penguin = Penguin("Penny", "Honk", 70)
dolphin = Dolphin("Flipper", "Ee-ee", 300)

# Демонстрация методов
print(dog.make_sound())  # Вывод: Buddy says Woof
print(dog.info())        # Вывод: Name: Buddy, Sound: Woof, Fur Color: Brown
print(dog.fetch())       # Вывод: Buddy is fetching the ball!

print(penguin.make_sound())  # Вывод: Penny says Honk
print(penguin.info())        # Вывод: Name: Penny, Sound: Honk, Wingspan: 70 cm
print(penguin.swim())        # Вывод: Penny is swimming!
print(penguin.do_not_fly())  # Вывод: Penny cannot fly.

print(dolphin.make_sound())  # Вывод: Flipper says Ee-ee
print(dolphin.info())        # Вывод: Name: Flipper, Sound: Ee-ee, Max Depth: 300 meters
print(dolphin.swim())        # Вывод: Flipper is swimming!
