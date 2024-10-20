def sum_of_positive_odd_numbers(numbers):

  for number in numbers:
    if number % 2 == 0 or number < 0:
      raise ValueError("Список содержит чётные или отрицательные числа.")
  return sum(numbers)

try:
  numbers1 = [1, 3, 5, 7, 9]
  result1 = sum_of_positive_odd_numbers(numbers1)
  print("Сумма:", result1)

  numbers2 = [1, 3, 5, 7, 0]
  result2 = sum_of_positive_odd_numbers(numbers2)
  print("Сумма:", result2)

  numbers3 = [1, 3, -5, 7, 9]
  result3 = sum_of_positive_odd_numbers(numbers3)
  print("Сумма:", result3)

except ValueError as e:
  print("Ошибка:", e)

input()