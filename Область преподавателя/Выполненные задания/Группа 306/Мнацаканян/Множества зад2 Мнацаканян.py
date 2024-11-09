# Задаем множества студентов и сотрудников
students = {"Tom", "Bob", "Sam"}
employees = {"Tom", "Bob", "Alex", "Mike"}

# Находим всех людей в обеих группах
all_people = students.union(employees)

# Находим всех, кто одновременно и учится, и работает
both_groups = students.intersection(employees)

# Находим только студентов, которые не работают
only_students = students.difference(employees)

# Находим людей, которые либо только учатся, либо только работают, но не одновременно
only_one_group = (students.difference(employees)).union(employees.difference(students))

# Вывод результатов
print("Все люди в обеих группах: ", all_people)
print("Люди, которые одновременно учатся и работают: ", both_groups)
print("Люди, которые только учатся, но не работают: ", only_students)
print("Люди, которые либо только учатся, либо только работают, но не одновременно: ", only_one_group)

input()