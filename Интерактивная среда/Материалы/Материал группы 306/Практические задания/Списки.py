# Задание 1
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
