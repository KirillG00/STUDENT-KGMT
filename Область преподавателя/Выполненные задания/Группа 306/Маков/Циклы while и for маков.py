sum_of_squares = 0

# Используем цикл for и функцию range для перебора чисел от 1 до 10
for number in range(1, 11):
    # Вычисляем квадрат текущего числа
    square = number ** 2

    sum_of_squares += square

# Выводим результат
print("Сумма квадратов чисел от 1 до 10 составляет:", sum_of_squares)
input()