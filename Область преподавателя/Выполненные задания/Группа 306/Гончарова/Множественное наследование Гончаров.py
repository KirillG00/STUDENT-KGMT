class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name}: {self.sound}")

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
        print("Ловит")

class NoFlyBird:
    def do_not_fly(self):
        print("Не может летать")

class Fish:
    def swim(self):
        print("Плавает")

class Dog(Mammal, Pet):
    def __init__(self, name, fur_color):
        super().__init__(name, "Гав", fur_color)

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Звук: {self.sound}")
        print(f"Цвет шерсти: {self.fur_color}")

class Penguin(Bird, Fish, NoFlyBird):
    def __init__(self, name, wingspan):
        super().__init__(name, "Квак", wingspan)

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Звук: {self.sound}")
        print(f"Размах крыльев: {self.wingspan}")

class Dolphin(MarineAnimal, Fish):
    def __init__(self, name, depth):
        super().__init__(name, "Клик", depth)

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Звук: {self.sound}")
        print(f"Максимальная глубина погружения: {self.depth}")

dog = Dog("Барбос", "коричневый")
penguin = Penguin("Пинг", 1.5)
dolphin = Dolphin("Дельфин", 200)

dog.make_sound()
dog.fetch()
penguin.make_sound()
penguin.swim()
penguin.do_not_fly()
dolphin.make_sound()
dolphin.swim()

print("\nИнформация о собаке:")
dog.info()
print("\nИнформация о пингвине:")
penguin.info()
print("\nИнформация о дельфине:")
dolphin.info()

input()