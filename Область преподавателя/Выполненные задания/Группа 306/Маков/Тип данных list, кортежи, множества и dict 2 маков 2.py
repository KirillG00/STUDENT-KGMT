people = [
    {"name": "Tom", "age": 39, "company": "SuperCorp", "languages": ["Python", "JavaScript"]},
    {"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "C++", "C#"]},
    {"name": "Sam", "age": 28, "company": "LittleCorp", "languages": ["Python", "Java"]}
]


for person in people:

    name = person["name"]

    last_language = person["languages"][-1]

    print(f"Name: {name}")
    print(f"Last language: {last_language}")
    

input()