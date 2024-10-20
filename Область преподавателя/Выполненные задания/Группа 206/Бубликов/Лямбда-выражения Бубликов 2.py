git = lambda x: x + 15

hab = lambda x, y: x * y

numbers = int(input("введите число:"))
print(f"{numbers} + 15 = {git(numbers)}")

x = int(input("введите x:"))
y = int(input("введите y:"))

print(f"{x} * {y} = {hab(x, y)}")

input()