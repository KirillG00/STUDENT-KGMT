#Задание5

# Создание списков
numbers = []
squares = []
cubes = []

# Цикл для заполнения списков
for i in range(1, 11):
    numbers.append(i)        # Добавление числа в список numbers
    squares.append(i**2)    # Добавление квадрата числа в список squares
    cubes.append(i**3)      # Добавление куба числа в список cubes

# Вывод результатов на консоль
print("numbers:", numbers)
print("squares:", squares)
print("cubes:", cubes)


#Задание6

# Начальный список
original_list = [10, 20, 30, 40, 50]

# Располагаем элементы в обратном порядке
reversed_list = original_list[::-1]

# Вывод результатов на консоль
print("Начальный список:", original_list)
print("Список в обратном порядке:", reversed_list)

input()