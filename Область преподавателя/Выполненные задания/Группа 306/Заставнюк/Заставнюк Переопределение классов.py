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
        print(f"{self.name} Приносит мяч")
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(self):
        print("мяу")
    def catching_mice(self):
        print(f"{self.name}, Ловит мышей ")
dog = Dog("ГлобГлобГабГалаб", 666)
cat = Cat("Ай лов букс", 4)



dog.bring_ball()
dog.make_sound()

cat.catching_mice()
cat.make_sound()


input()