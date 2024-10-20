class Actor:
    def __init__(self, name, age, famous_role, description):
        self.name = name
        self.age = age
        self.famous_role = famous_role
        self.description = description

    def info(self):
        return f"{self.name} {self.age} лет, был лучшим актером в фильме {self.famous_role}. {self.description}"

actors_list = [
    Actor("Томас Шелби", 43, "Острые козырки", "Крутой чел с крутой харизмой"),
    Actor("Мерлин монро", 29, "Какая та роль", "Тоже наверная крутая харизма"),
    Actor("Я самый лучший актер", 18, "Жизнь", "Создаю безвыходные ситуации, и выхожу из них")
]

for actor in actors_list:
    print(actor.info())

input()