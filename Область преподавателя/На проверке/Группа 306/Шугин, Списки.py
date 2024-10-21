# Исходный список имен
names = ["Tom", "Bob", "Sam"]

# Добавляем новые имена
names.extend(["Alice", "Kate"])

# Удаляем последнее имя
names.pop()  # Удаляет "Kate"

# Выводим финальный список
print(names)  # Вывод: ['Tom', 'Bob', 'Sam', 'Alice']

### Задание 2

# Задание 2: матрица
mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Выводим всю матрицу
print("mat:", mat)  # Вывод: [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

# Выводим каждую строку матрицы
for i in range(len(mat)):
    print(f"mat[{i}]: {mat[i]}")

# Выводим каждый элемент матрицы
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(f"mat[{i}][{j}]: {mat[i][j]}")

input()