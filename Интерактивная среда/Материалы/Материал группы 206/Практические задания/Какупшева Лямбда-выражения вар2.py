#Лямбда-выражение вар1
add_15 = lambda x: x + 15

multiply = lambda x, y: x * y

number = float(input("Введите число, к которому нужно добавить 15: "))
print(f"{number} + 15 = {add_15(number)}")

x = float(input("Введите первое число для умножения: "))
y = float(input("Введите второе число для умножения: "))
print(f"{x} * {y} = {multiply(x, y)}")
