# Начальный список
initial_list = [11, 22, 33, 44, 55]

# Новый список для нечетных чисел
odd_numbers = [num for num in initial_list if num % 2 != 0]

# Вывод на консоль
print("Начальный список:", initial_list)
print("Список с нечетными числами:", odd_numbers)

### Задание 8


def sum_lists(list1, list2):
    # Проверка на равенство длины списков
    if len(list1) != len(list2):
        raise ValueError("Списки должны быть одинаковой длины")

    # Сложение соответствующих элементов
    result = [a + b for a, b in zip(list1, list2)]
    return result


# Пример использования функции
first_list = [1, 2, 3, 4]
second_list = [5, 6, 7, 8]
result = sum_lists(first_list, second_list)

# Вывод на консоль
print("Первый список:", first_list)
print("Второй список:", second_list)
print("Результат сложения:", result)

input()