class Actor:
    def __init__(self, name, age, famous_role, description):
        self.name = name  # Имя актера
        self.age = age  # Возраст актера
        self.famous_role = famous_role  # Известная роль
        self.description = description  # Описание

    def __str__(self):

        return f"Имя: {self.name}, Возраст: {self.age}, Известная роль: {self.famous_role}, Описание: {self.description}"


actors = [
    Actor("Джонни Депп", 60, "Капитан Джек Воробей", "Знаменитый американский актер."),
    Actor("Мерил Стрип", 74, "Клара Стрэнд", "Одна из самых награждаемых актрис в мире."),
    Actor("Леонардо ДиКаприо", 48, "Джордж ДиКаприо", "Известен своими ролями в драматических фильмах.")
]

for actor in actors:
    print(actor)
 
input()