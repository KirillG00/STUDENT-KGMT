class Actor:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Actor Name: {self.name}"

# Создаем несколько объектов класса Actor
actor1 = Actor("Leonardo DiCaprio")
actor2 = Actor("Meryl Streep")
actor3 = Actor("Denzel Washington")
actor4 = Actor("Natalie Portman")

# Тестируем код через print
print(actor1)
print(actor2)
print(actor3)
print(actor4)

input()