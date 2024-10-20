class Person:
    def __init__(self, name, age, hobbies):
        self.name = name        # Имя
        self.age = age          # Возраст
        self.hobbies = hobbies  # Хобби

# Создаем два объекта класса Person
person1 = Person("Алексей", 30, ["фотография", "путешествия"])
person2 = Person("Мария", 25, ["чтение", "спорт"])

# Класс для описания книги
class Book:
    def __init__(self, title, author, genre):
        self.title = title      # Заголовок книги
        self.author = author    # Автор
        self.genre = genre      # Жанр

# Создаем два объекта класса Book
book1 = Book("1984", "Джордж Оруэлл", "антиутопия")
book2 = Book("Гарри Поттер", "Джоан Роулинг", "фэнтези")

# Класс для описания автомобиля
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand      # Марка автомобиля
        self.model = model      # Модель
        self.year = year        # Год выпуска

# Создаем два объекта класса Car
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Ford", "Focus", 2019)

# Класс для описания места
class Place:
    def __init__(self, name, location, type_of_place):
        self.name = name        # Название места
        self.location = location # Расположение
        self.type_of_place = type_of_place # Тип места

# Создаем два объекта класса Place
place1 = Place("Эйфелева башня", "Париж", "достопримечательность")
place2 = Place("Байкал", "Россия", "озеро")


class Animal:
    def __init__(self, species, age, habitat):
        self.species = species  #
        self.age = age
        self.habitat = habitat

animal1 = Animal("Кошка", 5, "домашний")
animal2 = Animal("Собака", 3, "домашний")

input()