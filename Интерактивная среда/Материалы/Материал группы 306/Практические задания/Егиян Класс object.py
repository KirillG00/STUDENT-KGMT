class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(self)

    def __str__(self):
        return f"Name: {self.name}  Age: {self.age}"

kir = person("карееееннннннн", 1845665665757555586786855654344344354334534545565565646)
print(kir)
kir.display_info()