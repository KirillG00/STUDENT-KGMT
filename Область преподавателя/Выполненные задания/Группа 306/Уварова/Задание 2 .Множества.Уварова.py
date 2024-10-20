# Задаем множества студентов и работников
students = {"Tom", "Bob", "Sam"}
employees = {"Tom", "Bob", "Alex", "Mike"}

# Все люди в обоих группах
all_people = students.union(employees)

# Люди, которые одновременно учатся и работают
both_students_and_employees = students.intersection(employees)

# Люди, которые только учатся, но не работают
only_students = students.difference(employees)

# Люди, которые только работают, но не учатся
only_employees = employees.difference(students)

# Люди, которые либо только учатся, либо только работают (но не одновременно)
exclusive_people = only_students.union(only_employees)

# Вывод результатов
print("Все люди в обеих группах:", all_people)
print("Одновременно и учатся, и работают:", both_students_and_employees)
print("Только учатся, но не работают:", only_students)
print("Только работают, но не учатся:", only_employees)
print("Люди, которые либо только учатся, либо только работают:", exclusive_people)