# Задание 3.Выведите элементы матрицы с помощью циклов
mat = [
[10, 20, 30],
[40, 50, 60],
[70, 80, 90]
]

for row in mat:
    for elem in row:
        print(elem, end=' ')
    print()

# Задание 4.Напишите программу, которая удаляет дубликаты из списка.
numbers = [10, 20, 10, 20, 30, 40, 30, 50]
unique_numbers = list(set(numbers))

print("Начальный список:", numbers)
print("После удаления дублей:", unique_numbers)

input()