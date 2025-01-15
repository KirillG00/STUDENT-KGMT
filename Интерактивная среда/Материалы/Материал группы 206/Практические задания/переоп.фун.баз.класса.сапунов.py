class Animal:

    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print(f"Это животное по имени {self.name} создает звук")

class Dog(Animal):

    def make_sound(self):
        super().make_sound()
        print('Bark')

    def bring_ball(self):
        print(f"{self.name} принес мяч")
class Cat(Animal):

    def make_sound(self):
        super().make_sound()
        print("meow")

    def watching_mice(self):
        print(f"{self.name} наблюдает за мышью")


dog = Dog(input("Введите имя: "))
cat = Cat(input("Введите имя: "))

cat.make_sound()
dog.make_sound()
cat.watching_mice()
dog.bring_ball()
