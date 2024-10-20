# Инициализация списков
numbers = []
squares = []
cubes = []

# Цикл для создания списков
for i in range(1, 11):
    numbers.append(i)
    squares.append(i ** 2)
    cubes.append(i ** 3)

# Вывод списков на консоль
print("numbers:", numbers)
print("squares:", squares)
print("cubes :", cubes)

### Задание 6

# Начальный список
initial_list = [10, 20, 30, 40, 50]

# Разворот списка
reversed_list = initial_list[::-1]

# Вывод на консоль
print("Начальный список:", initial_list)
print("Список в обратном порядке:", reversed_list)

input()