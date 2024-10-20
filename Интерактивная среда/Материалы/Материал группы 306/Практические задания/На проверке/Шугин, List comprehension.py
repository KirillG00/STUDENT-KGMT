
input()# Пример словаря
my_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6
}

# Выбор ключей, длина которых больше 3
keys_filtered = [key for key in my_dict.keys() if len(key) > 3]
print(keys_filtered)  # ['three', 'four', 'five']

input()