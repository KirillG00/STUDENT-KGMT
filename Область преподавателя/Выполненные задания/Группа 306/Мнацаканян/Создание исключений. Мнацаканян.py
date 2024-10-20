def sum_and_check(numbers):
    for num in numbers:
        if num % 2 == 0:
            raise ValueError("В списке не должно быть четных чисел")
        if num < 0:
            raise ValueError("В списке не должно быть отрицательных чисел")

    return sum(numbers)


# Примеры использования
try:
    result = sum_and_check(int(input("Введите список: ")))
    print(result)  # Вывод: 25
except ValueError as e:
    print(e)

input()