add_15 = lambda x: x + 15
multiply = lambda x, y: print(x * y)

number = int(input("Введите число: "))
result_add = add_15(number)
print(f"Результат добавления 15 к {number}: {result_add}")



x = int(input("Введите первое число для умножения: "))
y = int(input("Введите второе число для умножения: "))
multiply(x, y)

input()