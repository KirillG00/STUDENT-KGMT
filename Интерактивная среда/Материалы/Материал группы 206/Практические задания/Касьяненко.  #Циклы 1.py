#Циклы 1
while True:
    # Ввод первого числа
    first_number = input("Введите первое число: ")
    # Ввод второго числа
    second_number = input("Введите второе число: ")

    try:
        # Преобразование введенных значений в числа
        first_number = float(first_number)
        second_number = float(second_number)

        # Вычисление суммы
        total_sum = first_number + second_number
        print(f"Сумма чисел: {total_sum}")

    except ValueError:
        print("Пожалуйста, введите корректные числа.")
        continue  # Продолжает цикл, если ввод не является числом

    # Запрос на завершение программы
    exit_input = input("Нажмите Y или y для завершения программы: ")
    if exit_input.lower() == 'y':
        print("Завершение программы...")
        break  # Выход из бесконечного цикла
