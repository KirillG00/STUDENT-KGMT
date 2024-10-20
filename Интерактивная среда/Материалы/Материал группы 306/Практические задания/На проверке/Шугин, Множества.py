list1 = [10, 20, 30, 40, 50]
list2 = [20, 25, 30, 35, 40]

# Находим разность списков
difference = [item for item in list1 if item not in list2]
print("Разность списков:", difference)


### Задание 2

students = {"Tom", "Bob", "Sam"}
employees = {"Tom", "Bob", "Alex", "Mike"}

# Все люди в обеих группах
all_people = students.union(employees)
print("Все люди:", all_people)

# Люди, которые одновременно и учатся, и работают
both_groups = students.intersection(employees)
print("Одновременно учатся и работают:", both_groups)

# Люди, которые только учатся, но не работают
only_students = students.difference(employees)
print("Только студенты:", only_students)

# Люди, которые либо только учатся, либо только работают, но не одновременно
only_one_group = students.symmetric_difference(employees)
print("Люди только из одной группы:", only_one_group)

input()