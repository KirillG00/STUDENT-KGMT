def opera(a, b):
    сумма = a + b
    разность = a - b 
    умножение = a * b 
    if b != 0:
        деление = a/b 
    return (сумма, разность, умножение, деление)
result = opera(10, 2)
print(result)

input()