
# math_operations.py
def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b
def subtract(a, b):
    """Возвращает разность двух чисел."""
    return a - b
def multiply(a, b):
    """Возвращает произведение двух чисел."""
    return a * b
def divide(a, b):
    """Возвращает частное двух чисел, проверяя деление на ноль."""
    if b == 0:
        raise ValueError("Ошибка: Деление на ноль невозможно.")
    return a / b
def main():
    try:
        # Запрос числа у пользователя
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        # Запрос операции у пользователя
        operation = input("Выберите операцию (add, subtract, multiply, divide): ")

        # Выполнение соответствующей операции
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            print("Ошибка: Неверная операция.")
            return

        # Вывод результата
        print(f"Результат: {result}")

    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()