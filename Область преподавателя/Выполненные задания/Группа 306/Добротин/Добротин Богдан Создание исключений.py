def sum_of_list(numbers):
    """
    Вычисляет сумму чисел в списке.

    Args:
        numbers: Список целых чисел.

    Returns:
        Сумма чисел в списке.

    Raises:
        ValueError: Если в списке есть хотя бы одно чётное или отрицательное число.
    """

    for number in numbers:
        if number % 2 == 0 or number < 0:
            raise ValueError("Список содержит чётные или отрицательные числа.")

    return sum(numbers)

# Пример использования
try:
    numbers = [1, 3, 5, 7]
    result = sum_of_list(numbers)
    print(f"Сумма чисел: {result}")

except ValueError as e:
    print(f"Ошибка: {e}")

# Пример с ошибкой
try:
    numbers = [1, 3, 5, 2]
    result = sum_of_list(numbers)
    print(f"Сумма чисел: {result}")

except ValueError as e:
    print(f"Ошибка: {e}")
    
input()