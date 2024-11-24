people = [
    {"name": "Андрей", "age": 18, "company": "SuperCorp", "languages": ["Python", "JavaScript"]},
    {"name": "Максим", "age": 16, "company": "BigCorp", "languages": ["Python", "C++", "C#"]},
    {"name": "Сергей", "age": 22, "company": "LittleCorp", "languages": ["Python", "Java"]}
]

for person in people:
    print(f"Name: {person['name']}")
    print(f"Last language: {person['languages'][-1]}")
