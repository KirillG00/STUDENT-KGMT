from math_operations_Гончаров import add, subtract, multiply, divide, power

print("Введите первое число:")
num1 = float(input())
print("Введите второе число:")
num2 = float(input())
print("Выберите операцию (add, subtract, multiply, divide, power):")
operation = input()

if operation == "add":
    result = add(num1, num2)
    print("Результат:", result)
elif operation == "subtract":
    result = subtract(num1, num2)
    print("Результат:", result)
elif operation == "multiply":
    result = multiply(num1, num2)
    print("Результат:", result)
elif operation == "divide":
    result = divide(num1, num2)
    print("Результат:", result)
elif operation == "power":
    result = power(num1, num2)
    print("Результат:", result)
else:
    print("Ошибка: неверная операция")

input()
