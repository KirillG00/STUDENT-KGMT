students = {"Tom", "Bob", "Sam"}
employees = {"Tom", "Bob", "Alex", "Mike"}

all_people = students.union(employees)

both_groups = students.intersection(employees)

only_students = students.difference(employees)

only_students_or_employees = students.symmetric_difference(employees)

print(f"Все люди в обоих группах: {all_people}")
print(f"Люди, которые одновременно и учатся, и работают: {both_groups}")
print(f"Люди, которые только учатся, но не работают: {only_students}")
print(f"Люди, которые либо только учатся, либо только работают, но не одновременно: {only_students_or_employees}")
