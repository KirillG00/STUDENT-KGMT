class Actor:
    def __init__(self, name, age, known_role, description):
        self.name = name
        self.age = age
        self.known_role = known_role
        self.description = description

    def __str__(self):
        return (f"Actor(Name: {self.name}, Age: {self.age}, "
                f"Known Role: {self.known_role}, Description: {self.description})")

# Создание объектов для актеров
actor1 = Actor("Leonardo DiCaprio", 48, "Jack Dawson in Titanic",
                "Academy Award-winning actor known for his versatility and dedication to his craft.")
actor2 = Actor("Meryl Streep", 74, "Sophie Zawistowski in Sophie's Choice",
                "Widely regarded as one of the greatest actresses of all time, known for her outstanding performances.")

actor3 = Actor("Robert Downey Jr.", 58, "Tony Stark in Iron Man",
                "Iconic actor with a career resurgence in the Marvel Cinematic Universe.")
actor4 = Actor("Natalie Portman", 42, "Nina Sayers in Black Swan",
                "Academy Award-winning actress known for her roles in both independent and blockbuster films.")

# Проверка работы кода через print
print(actor1)
print(actor2)
print(actor3)
print(actor4)
