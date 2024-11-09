def diferencia_listas(list1, list2):
    return [item for item in list1 if item not in list2]

# Пример 1
list1 = [10, 20, 30, 40, 50]
list2 = [20, 25, 30, 35, 40]

resultado = diferencia_listas(list1, list2)
print("Разность списков: ", resultado)

input()