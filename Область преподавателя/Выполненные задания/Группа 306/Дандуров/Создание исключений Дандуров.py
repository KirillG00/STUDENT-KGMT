def zzz(numbers):

  for num in numbers:
    if num % 2 == 0 or num < 0:
      raise ValueError("В списке не должно быть чётных чисел или отрицательных чисел")

  return sum(numbers)

try:
  result = zzz([1, 3, 5, 7, 9])
  print(result)  
except ValueError as e:
  print(e)

try:
  result = zzz([1, 2, 5, 7, 9])
except ValueError as e:
  print(e)
try:
  result = zzz([1, -2, 5, 7, 9])
except ValueError as e:
  print(e)

input()