def compare_lists(list1, list2):
    difference = [item for item in list1 if item not in list2]
    return difference

list1 = [100, 200, 300, 400, 500]
list2 = [100, 250, 300, 330, 400]

result = compare_lists(list1, list2)

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"Разность списков: {result}")