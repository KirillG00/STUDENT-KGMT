import random


def calculate_hit():
    # Генерация случайного числа от 1 до 20
    base_roll = random.randint(1, 20)

    # Ввод модификатора с клавиатуры
    modifier = int(input("Введите модификатор попадания: "))

    # Расчет итогового значения попадания
    hit_result = base_roll + modifier
    print(f"Результат броска: {base_roll} + {modifier} = {hit_result}")

    # Ввод типа оружия
    weapon_type = input("Введите тип оружия (автомат/пп/пулемёт): ").strip().lower()

    if weapon_type in ["автомат", "пп", "пулемёт"]:
        # Генерация случайного числа от 1 до 20 для способности
        ability_roll = random.randint(1, 20)

        # Ввод модификатора способности с клавиатуры
        ability_modifier = int(input("Введите модификатор способности: "))

        # Расчет итогового значения способности
        ability_result = ability_roll + ability_modifier
        print(f"Результат броска способности: {ability_roll} + {ability_modifier} = {ability_result}")

        # Расчет процента попавших пуль
        hit_percentage = ability_result * 5
        print(f"Процент попавших пуль: {hit_percentage}%")
    else:
        print("Тип оружия не распознан. Программа завершена.")


if __name__ == "__main__":
    calculate_hit()