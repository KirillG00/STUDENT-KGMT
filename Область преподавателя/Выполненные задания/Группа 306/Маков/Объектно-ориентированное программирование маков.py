class Actors:
    def __init__(self, name):
        # Инициализируем имя актера
        self.name = name

    def __str__(self):
        # Метод для строкового представления объекта
        return self.name

# Создаем экземпляры класса для любимых актеров
actor1 = Actors("Кристиан Бэйл")
actor2 = Actors("Мерил Стрип")
actor3 = Actors("Леонардо ДиКаприо")

# Собираем имена актеров в список
favorite_actors = [actor1, actor2, actor3]

for actor in favorite_actors:
    print(actor)
    
input()