# Начальный список
initial_list = [10, 20, 10, 20, 30, 40, 30, 50]

# Удаление дубликатов с сохранением порядка
def remove_duplicates(input_list):
    seen = set()  # Множество для хранения уникальных элементов
    output_list = []  # Список для результата

    for item in input_list:
        if item not in seen:
            seen.add(item)  # Добавляем элемент в множество
            output_list.append(item)  # Добавляем элемент в результирующий список

    return output_list

# Удаляем дубликаты
result_list = remove_duplicates(initial_list)

# Вывод результата
print("Начальный список:", initial_list)
print("После удаления дублей:", result_list)

input()