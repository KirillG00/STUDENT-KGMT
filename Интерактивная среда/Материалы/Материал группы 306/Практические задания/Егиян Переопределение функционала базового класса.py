class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("Гавкает")

    def bring_ball(self):
        print(f"{self.name} приносит тапочки")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("Мявкает")

    def catching_mice(self):
        print(f"{self.name}, мурлыкает ")

dog = Dog("ГафГафыч", 3)
cat = Cat("МяуМяуч", 2)

dog.make_sound()
dog.bring_ball()

cat.make_sound()
cat.catching_mice()

input()