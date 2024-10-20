#Задани9

def dot_product(vector_a, vector_b):
    # Проверка на равенство длины векторов
    if len(vector_a) != len(vector_b):
        raise ValueError("Векторы должны быть одинаковой длины")

    # Вычисление скалярного произведения
    result = sum(a * b for a, b in zip(vector_a, vector_b))

    return result


# Примеры использования функции
first_vector = [1, 2, 3, 4]
second_vector = [5, 6, 7, 8]

result = dot_product(first_vector, second_vector)

# Вывод результата
print("Первый вектор:", first_vector)
print("Второй вектор:", second_vector)
print("Скалярное произведение:", result)

input()