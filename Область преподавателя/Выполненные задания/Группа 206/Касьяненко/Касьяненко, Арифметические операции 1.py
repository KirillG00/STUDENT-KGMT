def calculate_interest(P, R, T):
    return (P * R * T) / 100

P = float(input("Введите начальную сумму : "))
R = float(input("Введите процент по вкладу : "))
T = float(input("Введите количество лет : "))

interest = calculate_interest(P, R, T)

print(f"Накопленный процент за {T} лет составит: {interest}")

input()