a = int(input("Введите сумму продажи"))
if (a < 5000) :
    b = a * 0.05
    print(a - b)
if (a > 5001) and (a < 15000):
    b = a * 0.12
    print(a - b)
if (a > 15001) and (a <= 25000):
    b = a * 0.20
    print(a - b)
if (a > 25000) :
    b = a * 0.30
    print(a - b)

input()