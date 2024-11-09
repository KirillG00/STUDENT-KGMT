list1 = [10, 20, 30, 40, 50]
list2 = [20, 25, 30, 35, 40]

# Используем списковое включение для нахождения элементов, которые есть в list1, но отсутствуют в list2
difference = [item for item in list1 if item not in list2]

# Выводим результат
print("Разность списков:", difference)

input()
