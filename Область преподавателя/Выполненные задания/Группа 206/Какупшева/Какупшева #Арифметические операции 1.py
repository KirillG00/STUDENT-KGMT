#Арифметические операции 1
def calculate_interest(P, R, T):
    return (P * R * T) / 100

# Ввод данных
P = float(input("Введите начальную сумму (P): "))
R = float(input("Введите процент по вкладу (R): "))
T = float(input("Введите количество лет (T): "))

# Вычисление процентов
interest = calculate_interest(P, R, T)

print(f"Накопленный процент за {T} лет составит: {interest}")

input()