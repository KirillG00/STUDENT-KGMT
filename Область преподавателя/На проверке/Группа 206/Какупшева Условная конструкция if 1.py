# Функция для проверки, является ли год високосным
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Год високосный
            else:
                return False  # Год не високосный
        else:
            return True  # Год високосный
    else:
        return False  # Год не високосный

# Ввод года пользователем
year = int(input("Введите год: "))

# Проверка и вывод результата
if is_leap_year(year):
    print(f"Год {year} является високосным.")
else:
    print(f"Год {year} не является високосным.")
