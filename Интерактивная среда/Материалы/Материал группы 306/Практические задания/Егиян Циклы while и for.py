# Циклы while и for
# 1

n = 0
for i in range(1, 11):
    n += i ** 2
print(n)

# 2

i = 1
while i <= 10:
    print(i ** 2)
    i += 1

# 3

list = ["Python", "C++", "C#", "Fortran", "JavaScript"]
for i in list:
    print(f"Язык программирования: {i} ")

input()