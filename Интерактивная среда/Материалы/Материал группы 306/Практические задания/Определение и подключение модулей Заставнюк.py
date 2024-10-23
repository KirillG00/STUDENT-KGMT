from math_operations_Заставнюк import add, subtract, multiply, divide

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter operation (+ for addition, - for subtraction, * for multiplication, / for division): ")

if operation == '+':
    result = add(a, b)
elif operation == '-':
    result = subtract(a, b)
elif operation == '*':
    result = multiply(a, b)
elif operation == '/':
    result = divide(a, b)
else:
    result = "Error: invalid operation"

print("Result: ", result)

input()