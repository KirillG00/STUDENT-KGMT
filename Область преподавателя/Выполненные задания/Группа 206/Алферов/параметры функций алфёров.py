def sum_range(start, end):
  if start > end:
    start, end = end, start
  sum = 0
  for i in range(start, end + 1):
    sum += i
  return sum

start = int(input("Начало: "))
end = int(input("Конец: "))
result = sum_range(start, end)
print(f"Сумма чисел от {start} до {end}: {result}")

input()