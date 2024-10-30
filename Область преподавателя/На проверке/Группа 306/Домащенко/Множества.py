#1

list1 = [10, 20, 30, 40, 50]
list2 = [20, 25, 30, 35, 40]

difference_list = [x for x in list1 if x not in list2]

print("Разность списков:", difference_list)

#2
print()
students = {"Tom", "Bob", "Sam"}
employees = {"Tom", "Bob", "Alex", "Mike"}

people = students.union(employees)
print("Все мерзавцы:", people)
both_groups = students.intersection(employees)
print("Люди, которые и учатся, и работают:", both_groups)

both = {person for person in students if person in employees}
print("Люди, которые одновременно учатся и работают:", both)

only_students = students.difference(employees)
print("Люди, которые только учатся, но не работают:", only_students)

either_or = students.symmetric_difference(employees)
print("Люди, которые либо только учатся, либо только работают, но не одновременно:", either_or)

input()
