def calculate_discount(sale_amount):
    """Функция для вычисления суммы скидки."""
    if sale_amount <= 5000:
        discount_rate = 0.05  # 5%
    elif sale_amount <= 15000:
        discount_rate = 0.12  # 12%
    elif sale_amount <= 25000:
        discount_rate = 0.20  # 20%
    else:
        discount_rate = 0.30  # 30%

    discount_amount = sale_amount * discount_rate
    return discount_amount

# Ввод суммы продажи пользователем
try:
    sale_amount = float(input("Введите сумму продажи: "))
    
    if sale_amount < 0:
        print("Сумма продажи не может быть отрицательной.")
    else:
        discount = calculate_discount(sale_amount)
        print(f"Сумма скидки: {discount:.2f}")
except ValueError:
    print("Пожалуйста, введите корректное число.")
    
    '''
    После вычисления скидки 
    программа должна вывести саму скидку и сумму с вычетом скидки. Выодится только
    сама скидка
    '''
    
input()