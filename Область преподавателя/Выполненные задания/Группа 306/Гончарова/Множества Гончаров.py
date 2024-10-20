# №1

list1 = [10, 20, 30, 40, 50]
list2 = [20, 25, 30, 35, 40]
difference_list = [x for x in list1 if x not in list2]
print("Разность списков: ", difference_list)
print()

# №2

students = {"Tom", "Bob", "Sam"}
employees = {"Tom", "Bob", "Alex", "Mike"}
people = students.union(employees)
print("Все люди в обоих группах:", people)

studying_working = set()
for person in students:
    if person in employees:
        studying_working.add(person)
print("Люди, которые одновременно и учатся и работают:", studying_working)

only_studying = students.difference(employees)
print("Люди, которые только учатся, но не работают:", only_studying)

either_or = students.symmetric_difference(employees)
print("Люди, которые либо только учатся, либо только работают, но не одновременно:", either_or)

input()