class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}"

    def info(self):
        return f"Animal Name: {self.name}, Sound: {self.sound}"


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
        return f"{super().info()}, Wingspan: {self.wingspan}"


class MarineAnimal(Animal):
    def __init__(self, name, sound, depth):
        super().__init__(name, sound)
        self.depth = depth

    def info(self):
        return f"{super().info()}, Max Depth: {self.depth} meters"


class Pet:
    def fetch(self):
        return f"{self.name} не умеет играть с мячик!"


class NoFlyBird:
    def do_not_fly(self):
        return f"{self.name} не умеет летать."


class Fish:
    def swim(self):
        return f"{self.name} плавает!"


class Dog(Mammal, Pet):
    def __init__(self, name, sound, fur_color):
        Mammal.__init__(self, name, sound, fur_color)


class Penguin(Bird, Fish, NoFlyBird):
    def __init__(self, name, sound, wingspan):
        Bird.__init__(self, name, sound, wingspan)
        self.name = name


class Dolphin(MarineAnimal, Fish):
    def __init__(self, name, sound, depth):
        MarineAnimal.__init__(self, name, sound, depth)
        self.name = name



dog = Dog("Бублик", "Гав гав тяф тяф", "коричнево-бежевый")
penguin = Penguin("Пигви", "сквик сквик сквик", "100 см")
dolphin = Dolphin("Дильфимильфи", "квквквквквкв", 3894)


print(dog.make_sound())
print(dog.fetch())
print(dog.info())

print(penguin.make_sound())
print(penguin.swim())
print(penguin.do_not_fly())
print(penguin.info())

print(dolphin.make_sound())
print(dolphin.swim())
print(dolphin.info())

input()