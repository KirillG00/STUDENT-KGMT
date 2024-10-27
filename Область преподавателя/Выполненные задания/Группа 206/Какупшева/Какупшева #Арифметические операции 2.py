#Арифметические операции 2
def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32

# Ввод данных
celsius = float(input("Введите температуру в градусах Цельсия: "))

# Перевод
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}°C равно {fahrenheit}°F")

input()
