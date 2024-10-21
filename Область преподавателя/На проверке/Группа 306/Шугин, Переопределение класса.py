class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some sound"

    def info(self):
        return f"Animal: {self.name}"


class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def info(self):
        return f"{super().info()}, Fur Color: {self.fur_color}"


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def info(self):
        return f"{super().info()}, Wingspan: {self.wingspan} cm"


class MarineAnimal(Animal):
    def __init__(self, name, depth):
        super().__init__(name)
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
    def __init__(self, name, fur_color):
        Mammal.__init__(self, name, fur_color)

    def make_sound(self):
        return "Woof!"

    def bring_ball(self):
        return f"{self.name} brings the ball!"


class Cat(Mammal):
    def __init__(self, name, fur_color):
        Mammal.__init__(self, name, fur_color)

    def make_sound(self):
        return "Meow!"

    def catching_mice(self):
        return f"{self.name} is catching mice!"


class Penguin(Bird, Fish, NoFlyBird):
    def __init__(self, name, wingspan):
        Bird.__init__(self, name, wingspan)

    def make_sound(self):
        return "Squawk!"

    def swim(self):
        return f"{self.name} is swimming!"


class Dolphin(MarineAnimal, Fish):
    def __init__(self, name, depth):
        MarineAnimal.__init__(self, name, depth)

    def make_sound(self):
        return "Click!"

    def swim(self):
        return f"{self.name} is swimming!"


# Создание экземпляров классов
dog = Dog(name="Buddy", fur_color="Brown")
cat = Cat(name="Whiskers", fur_color="White")
penguin = Penguin(name="Pingu", wingspan=90)
dolphin = Dolphin(name="Dolly", depth=300)

# Вызов методов
print(dog.make_sound())  # Вывод: Woof!
print(dog.fetch())  # Вывод: Buddy is fetching the ball!
print(dog.bring_ball())  # Вывод: Buddy brings the ball!
print(dog.info())  # Вывод: Animal: Buddy, Fur Color: Brown

print(cat.make_sound())  # Вывод: Meow!
print(cat.catching_mice())  # Вывод: Whiskers is catching mice!
print(cat.info())  # Вывод: Animal: Whiskers, Fur Color: White

print(penguin.make_sound())  # Вывод: Squawk!
print(penguin.swim())  # Вывод: Pingu is swimming!
print(penguin.info())  # Вывод: Animal: Pingu, Wingspan: 90 cm

print(dolphin.make_sound())  # Вывод: Click!
print(dolphin.swim())  # Вывод: Dolly is swimming!
print(dolphin.info())  # Вывод: Animal: Dolly, Max Depth: 300 m

input()