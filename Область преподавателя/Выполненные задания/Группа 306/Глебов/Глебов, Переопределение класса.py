# Базовый класс Animal
class Animal:
    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределён в подклассе")

# Подкласс Dog
class Dog(Animal):
    def make_sound(self):
        return "Гав!"

    def bring_ball(self):
        return "Собака приносит мяч."

# Подкласс Cat
class Cat(Animal):
    def make_sound(self):
        return "Мяу!"

    def catching_mice(self):
        return "Кошка ловит мышей."

# Пример использования
dog = Dog()
print(dog.make_sound())  # Вывод: Гав!
print(dog.bring_ball())  # Вывод: Собака приносит мяч.

cat = Cat()
print(cat.make_sound())  # Вывод: Мяу!
print(cat.catching_mice())  # Вывод: Кошка ловит мышей.

input()