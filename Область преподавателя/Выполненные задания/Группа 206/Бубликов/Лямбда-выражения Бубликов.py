git = lambda x: x + 15

hab = lambda x, y: x * y

numbers = int(input())
print(f"{numbers} + 15 = {git(numbers)}")

x = int(input())
y = int(input())

print(f"{x} * {y} = {hab(x, y)}")