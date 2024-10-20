import random


def calculate_hit():
    # Генерация случайного числа от 1 до 20
    d20 = random.randint(1, 20)

    # Ввод количества выстрелов
    shots = int(input("Введите количество выстрелов: "))

    # Ввод класса защиты
    defense_class = int(input("Введите класс защиты: "))

    # Ввод модификатора
    modifier = int(input("Введите модификатор попадания: "))

    # Ввод модификатора способности с клавиатуры
    ability_modifier = int(input("Введите модификатор способности: "))

    # Расчет значения попадания
    hit_result = d20 + modifier + ability_modifier
    print(f"Результат броска: {d20} + {modifier} + {ability_modifier}= {hit_result}")

    # Сравнение результата с классом защиты
    if d20 + ability_modifier  < defense_class:
        print("Результат меньше класса защиты. Программа завершена.")
        return
        print("Результат больше или равен классу защиты. Продолжайте.")

    # Расчет процента попавших пуль
    hit_percentage = min(hit_result * 5, 100)
    print(f"Процент попавших пуль: {hit_percentage}%")

    # Расчет количества попавших пуль
    hits = round((hit_percentage / 100) * shots)
    print(f"Количество попавших пуль: {hits}")


if __name__ == "__main__":
    calculate_hit()
