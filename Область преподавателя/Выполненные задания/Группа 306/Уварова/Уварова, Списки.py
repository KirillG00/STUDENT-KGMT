#Задание1
# Исходный список имен
names = ["Tom", "Bob", "Sam"]

# Имена, которые нужно добавить
new_names = ["Alice", "Kate"]

# Добавляем новые имена в список
names.extend(new_names)

# Удаляем последнее имя из списка
names.pop()

# Выводим финальный список
print(names)  # ['Tom', 'Bob', 'Sam', 'Alice']



#Задание2
# Матрица
mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Вывод всей матрицы в одном выражении
print(mat)

# Вывод по отдельности каждой строки матрицы
for row in mat:
    print(row)

# Вывод по отдельности каждого элемента матрицы
for row in mat:
    for element in row:
        print(element)

input()