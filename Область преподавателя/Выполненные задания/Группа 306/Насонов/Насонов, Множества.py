# Задание 1.
def difference_lists(list1, list2):
    result = [item for item in list1 if item not in list2]
    return result

list1 = [10, 20, 30, 40, 50]
list2 = [20, 25, 30, 35, 40]
result = difference_lists(list1, list2)
print(f"Разность списков: {result}")

# Задание 2
students = {"Tom", "Bob", "Sam"}
employees = {"Tom", "Bob", "Alex", "Mike"}

all_people = students.union(employees)

both_students_and_employees = students.intersection(employees)

students_only = students.difference(employees)

either_students_or_employees = students.symmetric_difference(employees)

print(f"Все люди в обеих группах: {all_people}")
print(f"Люди, которые одновременно и учатся, и работают: {both_students_and_employees}")
print(f"Люди, которые только учатся, но не работают: {students_only}")
print(f"Люди, которые либо только учатся, либо только работают, но не одновременно: {either_students_or_employees}")

input()