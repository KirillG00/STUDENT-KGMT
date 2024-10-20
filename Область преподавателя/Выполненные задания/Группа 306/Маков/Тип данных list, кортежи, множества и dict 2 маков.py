programmers = [
    {"name": "Tom", "languages": ["Python", "JavaScript"]},
    {"name": "Bob", "languages": ["C#", "Java"]},
    {"name": "Sam", "languages": ["Java", "C++"]}
]

for programmer in programmers:

    name = programmer["name"]

    last_language = programmer["languages"][-1]

    print(f"Name:  {name}")
    print(f"Last language:  {last_language}")
    
input()