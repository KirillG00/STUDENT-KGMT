students = {"Tom", "Bob", "Sam"}
employees = {"Tom", "Bob", "Alex", "Mike"}


all_people = students.union(employees)


both_students_and_employees = students.intersection(employees)


only_students = students.difference(employees)


only_one_group = students.symmetric_difference(employees)

# Вывод результатов
print("Все люди в обеих группах:", all_people)
print("Люди, которые одновременно учатся и работают:", both_students_and_employees)
print("Люди, которые только учатся:", only_students)
print("Люди, которые только учатся или только работают:", only_one_group)