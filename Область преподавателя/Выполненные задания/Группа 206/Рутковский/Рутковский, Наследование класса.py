class Animal:
    def __init__(self, name, age):
        self.name = name  # Имя животного
        self.age = age    # Возраст животного

    def info(self):
        """Метод для получения информации о животном."""
        return f"{self.name} is {self.age} years old."

# Подкласс Dog
class Dog(Animal):
    def bark(self):
        """Метод, который заставляет собаку лаять."""
        return f"{self.name} says Woof!"

# Подкласс Cat
class Cat(Animal):
    def meow(self):
        """Метод, который заставляет кошку мяукать."""
        return f"{self.name} says Meow!"

# Подкласс Bird
class Bird(Animal):
    def chirp(self):
        """Метод, который заставляет птицу чирикать."""
        return f"{self.name} says Chirp!"

# Создание объектов разных классов
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)
bird = Bird("Tweety", 1)

# Демонстрация использования методов
print(dog.info())  # Вывод: Buddy is 3 years old.
print(dog.bark())  # Вывод: Buddy says Woof!

print(cat.info())  # Вывод: Whiskers is 2 years old.
print(cat.meow())  # Вывод: Whiskers says Meow!

print(bird.info())  # Вывод: Tweety is 1 years old.
print(bird.chirp())  # Вывод: Tweety says Chirp!

input()