def sum(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
 
 
def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply
 
operation = select_operation(1)     # operation = sum
print(operation(10, 6))             # 16
 
operation = select_operation(2)     # operation = subtract
print(operation(10, 6))             # 4
 
operation = select_operation(3)     # operation = multiply
print(operation(10, 6))             # 60

input()