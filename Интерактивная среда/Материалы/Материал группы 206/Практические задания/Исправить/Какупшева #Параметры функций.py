#Параметры функций
def sum_range(start, end):
    # Проверка и замена местами, если start больше end
    if start > end:
        start, end = end, start

    total_sum = sum(range(start, end + 1))  # Сумма чисел от start до end включительно
    return total_sum

# Пример использования
result = sum_range(5, 10)
print(f"Сумма чисел от 5 до 10: {result}")

result = sum_range(10, 5)
print(f"Сумма чисел от 10 до 5: {result}")

input()