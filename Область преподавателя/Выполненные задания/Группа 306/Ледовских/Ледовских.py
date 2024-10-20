def summ(number):
    sum = 0
    for num in number:
        if num % 2 == 0:
            raise ValueError("четное")
        elif num < 0:
            raise ValueError("отрицательное в спсике")
        sum += num
    return sum


try:
    number = [1,-3]
    result = summ(number)
    print("Сумма", result)
except ValueError as e:
    print("Ошибка:", e)

input()