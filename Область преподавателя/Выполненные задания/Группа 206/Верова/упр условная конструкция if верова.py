amount = int(input('Введите сумму продажи: '))
if amount >0:
    if amount>25000:
        discount=amount *0.3
    elif amount>15000:
        discount=amount *0.2
    elif amount>5000:
        discount=amount*0.12
    else:
        discount=amount*0.5
    print('Скидка: ', discount)
    print('Сумма с учетом скидки: ', amount-discount)
else:
    print('Некорректная суммма')