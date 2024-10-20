list1 = [10, 20, 30, 40, 50]
list2 = [20, 25, 30, 35, 40]
dif_list = [x for x in list1 if x not in list2]
print("Разность списков: ", dif_list)
print()

students = {"Tom", "Bob", "Sam"}
employees = {"Tom", "Bob", "Alex", "Mike"}
people = students.union(employees)
print("Все люди в группах: ", people)

studying_working = set()
for person in students:
    if person in employees:
        studying_working.add(person)
print("Люди которые работают и учатся: ", studying_working)

only_studying = students.difference(employees)
print("Люди которые только учатся: ", only_studying)

either_or = students.symmetric_difference(employees)
print("Люди которые только учатся либо работают: ", either_or)

input()