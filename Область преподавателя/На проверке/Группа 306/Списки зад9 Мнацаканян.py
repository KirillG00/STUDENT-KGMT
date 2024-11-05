def sum_lists(list1, list2):
    # Проверка на равенство длины списков
    if len(list1) != len(list2):
        raise ValueError("Списки должны быть одинаковой длины")

    # Создание нового списка с суммами элементов
    summed_list = [a + b for a, b in zip(list1, list2)]

    return summed_list


# Примеры использования функции
first_list = [1, 2, 3, 4]
second_list = [5, 6, 7, 8]

result = sum_lists(first_list, second_list)

# Вывод результата
print("Первый список:", first_list)
print("Второй список:", second_list)
print("Результат сложения:", result)
