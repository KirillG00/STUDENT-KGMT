person_info = {
    "name": "Андрей",
    "age": 18,
    "company": "-",
    "programming_languages": ["Python", "JavaScript"]
}

print(f"Имя: {person_info['name']}")
print(f"Возраст: {person_info['age']} лет")
print(f"Компания: {person_info['company']}")
print(f"Используемые языки программирования: {', '.join(person_info['programming_languages'])}")
