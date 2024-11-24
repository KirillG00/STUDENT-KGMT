def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32

celsius = float(input("Введи температуру в градусах Цельсия: "))

fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}°C равно {fahrenheit}°F")