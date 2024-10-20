def difference_between_lists(list1, list2):
    return [element for element in list1 if element not in list2]

list1 = [10, 20, 30, 40, 50]
list2 = [20, 25, 30, 35, 40]

print("Разность списков:", difference_between_lists(list1, list2))
def difference_between_lists(list1, list2):
    return list(set(list1) - set(list2))

list1 = [10, 20, 30, 40, 50]
list2 = [20, 25, 30, 35, 40]

print("Разность списков:", difference_between_lists(list1, list2))


#задание 2
students = {"Tom", "Bob", "Sam"}
employees = {"Tom", "Bob", "Alex", "Mike"}

# Всех людей в обоих группах
all_people = students.union(employees)
print("Всех людей в обоих группах:", all_people)

# Всех людей, которые одновременно и учатся, и работают
both_students_and_employees = students.intersection(employees)
print("Всех людей, которые одновременно и учатся, и работают:", both_students_and_employees)

# Всех людей, которые только учатся, но не работают
only_students = students - employees
print("Всех людей, которые только учатся, но не работают:", only_students)

# Всех людей, которые либо только учатся, либо только работают, но не одновременно
only_one_group = (students - employees) | (employees - students)
print("Всех людей, которые либо только учатся, либо только работают, но не одновременно:", only_one_group)

input()