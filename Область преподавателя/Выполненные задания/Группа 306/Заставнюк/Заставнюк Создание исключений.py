def sum_of_list(numbers):

    for number in numbers:
        if number % 2 == 0 or number < 0:
            raise ValueError("Список содержит чётные или отрицательные числа.")

    return sum(numbers)

try:
    numbers = [1, 3, 5, 9]
    result = sum_of_list(numbers)
    print(f"Сумма чисел: {result}")

except ValueError as e:
    print(f"Ошибка: {e}")

try:
    numbers = [1, 3, 5, 2]
    result = sum_of_list(numbers)
    print(f"Сумма чисел: {result}")

except ValueError as e:
    print(f"Ошибка: {e}")