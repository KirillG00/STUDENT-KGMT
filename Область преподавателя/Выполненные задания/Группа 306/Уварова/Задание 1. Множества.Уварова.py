def compare_lists(list1, list2):
    result = [item for item in list1 if item not in list2]
    return result

# Пример использования
first_list = [1, 2, 3, 4, 5]
second_list = [4, 5, 6, 7]

difference = compare_lists(first_list, second_list)
print("Элементы из первого списка, которые отсутствуют во втором:", difference)
input()