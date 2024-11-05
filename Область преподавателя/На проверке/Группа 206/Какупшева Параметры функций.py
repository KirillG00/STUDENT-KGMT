def sum_range(start, end):
    # Проверка и замена местами, если start больше end
    if start > end:
        start, end = end, start

    total_sum = sum(range(start, end + 1))  # Сумма чисел от start до end включительно
    return total_sum

# Пример использования
try:
    start = int(input("Введите начальное число: "))
    end = int(input("Введите конечное число: "))

    result = sum_range(start, end)
    print(f"Сумма чисел от {start} до {end}: {result}")
except ValueError:
    print("Пожалуйста, введите корректные целые числа.")
