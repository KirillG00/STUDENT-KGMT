def oper(a, b):
    cумма = a + b
    разность = a - b
    умножение = a * b
    if b != 0:
        деление = a/b
    return (cумма, разность, умножение, деление)
result = oper(10,2)
print(result)
