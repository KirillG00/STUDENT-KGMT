def oper(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else None 
    
    return addition, subtraction, multiplication, division

result = oper(10, 2)
print(result)

input()