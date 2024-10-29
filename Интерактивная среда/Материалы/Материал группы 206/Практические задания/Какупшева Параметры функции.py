def sum_range(start, end):
    if start > end:
        start, end = end, start

    total_sum = sum(range(start, end + 1))
    return total_sum
result = sum_range(5000, 1000)
print(f"Сумма чисел от 5000 до 1000: {result}")

result = sum_range(1000, 500)
print(f"Сумма чисел от 1000 до 500: {result}")