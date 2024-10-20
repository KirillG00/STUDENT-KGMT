person_info = {
    "name": "Том",  # Имя человека
    "age": 39,      # Возраст человека
    "company": "SuperCorp", 
    "programming_languages": ["Python", "JavaScript"]
}

print("Имя:", person_info["name"])
print("Возраст:", person_info["age"])
print("Компания:", person_info["company"])
print("Языки программирования:", ", ".join(person_info["programming_languages"]))

input()