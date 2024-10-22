

from math_operations import add, subtract, multiply, divide, power

def main():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        operation = input("Выберите операцию (add, subtract, multiply, divide, power): ")

        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        elif operation == "power":
            result = power(a, b)
        else:
            print("Ошибка: Неверная операция.")
            return

        print(f"Результат: {result}")

    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
