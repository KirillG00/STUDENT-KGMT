def sum_of_integers(numbers):
    for number in numbers:
        # Проверяем на чётное число
        if number % 2 == 0:
            raise ValueError("В списке не должно быть чётных чисел")
        # Проверяем на отрицательное число
        if number < 0:
            raise ValueError("В списке не должно быть отрицательных чисел")

    # Если список прошёл проверку, возьмём его сумму
    return sum(numbers)


# Примеры использования
try:
    numbers1 = [1, 3, 5, 7, 9]
    print(sum_of_integers(numbers1))  # Вывод: 25

    numbers2 = [1, 2, 5, 7, 9]
    print(sum_of_integers(numbers2))  # В этом случае будет вызвано исключение

except ValueError as e:
    print(e)

try:
    numbers3 = [1, -2, 5, 7, 9]
    print(sum_of_integers(numbers3))  # В этом случае также будет вызвано исключение

except ValueError as e:
    print(e)

input()