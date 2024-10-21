class Person:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age}, Hobby: {self.hobby})"


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"Car(Brand: {self.brand}, Model: {self.model}, Year: {self.year})"


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book(Title: {self.title}, Author: {self.author}, Pages: {self.pages})"


class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

    def __str__(self):
        return f"Animal(Species: {self.species}, Name: {self.name}, Age: {self.age})"


class House:
    def __init__(self, address, size, num_rooms):
        self.address = address
        self.size = size  # in square meters
        self.num_rooms = num_rooms

    def __str__(self):
        return f"House(Address: {self.address}, Size: {self.size} sqm, Rooms: {self.num_rooms})"


# Создание объектов для классов

# Для класса Person
person1 = Person("Alice", 30, "Reading")
person2 = Person("Bob", 25, "Cycling")

# Для класса Car
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2018)

# Для класса Book
book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)

# Для класса Animal
animal1 = Animal("Dog", "Buddy", 5)
animal2 = Animal("Cat", "Whiskers", 3)

# Для класса House
house1 = House("123 Main St", 120, 3)
house2 = House("456 Elm St", 150, 4)

# Тестируем код через print
print(person1)
print(person2)
print(car1)
print(car2)
print(book1)
print(book2)
print(animal1)
print(animal2)
print(house1)
print(house2)

input()