ten = int(input('Введите сумму продажи:'))
if ten > 0:
    if ten > 25000:
        discount = ten * 0.3
    elif ten >  15000:
        discount = ten * 0.2
    elif ten > 5000:
        discount = ten * 0.12
    else:
        discount = ten * 0.05
    print('Скидка:', discount)
    print("Сумма с учетом скидки:",ten - discount)
else:
        print('Некоректная сумма')
        
input()