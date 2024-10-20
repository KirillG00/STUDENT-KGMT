print("Ввод: 10, 2")
def oper(a, b):
    сумма = a + b
    разность = a - b
    произведение = a * b
    частное = a / b
    return сумма, разность, произведение, частное

result = oper(10, 2)
print(f"Вывод: {result}")
input()
