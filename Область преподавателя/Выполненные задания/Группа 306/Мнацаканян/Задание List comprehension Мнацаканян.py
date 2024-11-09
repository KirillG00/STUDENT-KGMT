# Задаем словарь
my_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seventy": 70
}

# Выбираем только ключи длиной больше 3
filtered_keys = [key for key in my_dict.keys() if len(key) > 3]

# Вывод результата
print(filtered_keys)  # ['three', 'four', 'five', 'seventy']

input()