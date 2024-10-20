def calculate_interest(principal, rate, time):
    return print((principal * rate * time) / 100)
try:
    P = float(input("Начальная сумма вклада: "))
    R = float(input("Начисленные проценты: "))
    T = float(input("Количество лет: "))
    interest = calculate_interest(P, R, T)
except ValueError:
    print("Пожалуйста, введите корректные числовые значения.")

input()