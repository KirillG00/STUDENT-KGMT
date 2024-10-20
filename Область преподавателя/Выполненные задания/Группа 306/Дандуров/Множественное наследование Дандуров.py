class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} издает такой звук: {self.sound}")

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
        print("Приносит мяч!")

class NoFlyBird(Bird):
    def do_not_fly(self):
        print(f"{self.name} это птица,не летает.")

class Fish:
    def swim(self):
        print(f"{self.name} плавает.")

class Dog(Mammal, Pet):
    def __init__(self, name, sound, fur_color):
        super().__init__(name, sound, fur_color)

    def info(self):
        print(f"Собака: Его зовут: {self.name}, Звук: {self.sound}, Цвет: {self.fur_color}")

class Penguin(Bird, Fish):
    def __init__(self, name, sound, wingspan):
        super().__init__(name, sound, wingspan)

    def info(self):
        print(f"Пингвин: Его зовут: {self.name}, Звук: {self.sound}, Размах крыльев: {self.wingspan}см")

class Dolphin(MarineAnimal, Fish):
    def __init__(self, name, sound, depth):
        super().__init__(name, sound, depth)

    def info(self):
        print(f"Дельфин: Его зовут: {self.name}, Звук: {self.sound}, Плавает на глубине: {self.depth}м")

dog = Dog("Бобик", "Гав", "Черный")
penguin = Penguin("Бублик", "Квакает", 50)
dolphin = Dolphin("Карен", "Ты че тип?", 200)

dog.make_sound()
dog.fetch()
dog.info()

penguin.make_sound()
penguin.swim()
penguin.info()

dolphin.make_sound()
dolphin.swim()
dolphin.info()

input()