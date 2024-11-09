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

input()