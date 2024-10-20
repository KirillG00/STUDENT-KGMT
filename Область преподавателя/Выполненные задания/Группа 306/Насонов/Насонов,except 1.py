def sur_nam(numbers):
    bob = 0
    for num in numbers:
        if num % 2 == 0:
            raise ValueError(" В списке не должно быть чётных чисел")
        elif num < 0:
            raise ValueError("В списке не должно быть отрицательных чисел")
        bob += num
    return bob
# просто вывод
numbers = [1, 3, 5, 7, 9]
try:
    result = sur_nam(numbers)
    print(result)
except ValueError as e:
    print(e)
# с отрицательным
numbers = [-1, 2, 5, 7, 9]
try:
    print(sur_nam(numbers))
except ValueError as e:
    print(e)
# с четным
numbers = [1, 2, 5, 7, 9]
try:
    print(sur_nam(numbers))
except ValueError as e:
    print(e)