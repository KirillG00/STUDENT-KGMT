
def sum_of_integers(numbers):
    # Проверяем каждый элемент в списке
    for number in numbers:
        # Если число четное или отрицательное, вызываем исключение
        if number % 2 == 0 or number < 0:
            raise ValueError("Список содержит четное или отрицательное число.")

    # Если все числа подходят, возвращаем их сумму
    return sum(numbers)

# Пример использования функции
try:
    # Создаем список целых чисел
    integer_list = [1, -1, 3, 5, 7]
    # Вызываем функцию
    result = sum_of_integers(integer_list)
    print("Сумма чисел:", result)
except ValueError as e:
    # Обрабатываем исключение и выводим сообщение об ошибке
    print(e)

input()