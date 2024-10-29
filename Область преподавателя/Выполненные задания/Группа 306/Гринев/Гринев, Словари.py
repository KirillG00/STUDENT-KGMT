### Задание 1

# Создаем словарь с информацией о человеке
person = {
    "name": "Tom",
    "age": 39,
    "company": "SuperCorp",
    "languages": ["Python", "JavaScript"]
}

# Выводим информацию из словаря на консоль
print("Name:", person["name"])
print("Age:", person["age"])
print("Company:", person["company"])
print("Languages:", ", ".join(person["languages"]))


### Задание 2

# Даем список словарей с информацией о программистах
people = [
    {"name": "Tom", "age": 39, "company": "SuperCorp", "languages": ["Python", "JavaScript"]},
    {"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "C++", "C#"]},
    {"name": "Sam", "age": 28, "company": "LittleCorp", "languages": ["Python", "Java"]}
]

# Выводим имя и последний язык программирования из каждого словаря
for person in people:
    print("Name:", person["name"])
    print("Last language:", person["languages"][-1])  # Получаем последний язык

input()