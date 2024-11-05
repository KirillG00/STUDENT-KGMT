# Начальный список
original_list = [11, 22, 33, 44, 55]

# Фильтрация списка для удаления четных чисел
odd_list = [num for num in original_list if num % 2 != 0]

# Вывод результатов на консоль
print("Начальный список:", original_list)
print("Список с нечетными числами:", odd_list)
