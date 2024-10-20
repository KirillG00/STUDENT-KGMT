# Определяем базовый класс Animal
class Animal:
    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен")

# Наследуем класс Dog от Animal
class Dog(Animal):
    def make_sound(self):
        return "Гав!"

    def bring_ball(self):
        return "Собака приносит мяч!"

# Наследуем класс Cat от Animal
class Cat(Animal):
    def make_sound(self):
        return "Мяу!"

    def catch_mice(self):
        return "Кошка ловит мышей!"

# Наследуем класс Cow от Animal
class Cow(Animal):
    def make_sound(self):
        return "Му!"

    def produce_milk(self):
        return "Корова дает молоко!"

# Тестирование классов
dog = Dog()
cat = Cat()
cow = Cow()

print(dog.make_sound())        # Вывод: Гав!
print(dog.bring_ball())        # Вывод: Собака приносит мяч!
print(cat.make_sound())        # Вывод: Мяу!
print(cat.catch_mice())        # Вывод: Кошка ловит мышей!
print(cow.make_sound())        # Вывод: Му!
print(cow.produce_milk())      # Вывод: Корова дает молоко!

input()