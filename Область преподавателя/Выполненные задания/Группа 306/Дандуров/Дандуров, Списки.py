
print("#1")

people = ["Tom", "Bob", "Sam"]

people.append("Alice")
people.append("Kate")
#removed_item = people.pop(3)
last_item = people.pop()

print(people)

print("#2")

mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(mat)

for row in mat:
    print(row)

for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(f"mat[{i}][{j}]: {mat[i][j]}")


print("#3")

mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for row in mat:
    for element in row:
        print(element, end=" ")
    print()

print("#4")

def remove_duplicates(list1):

  return list(dict.fromkeys(list1))

initial_list = [10, 20, 10, 20, 30, 40, 30, 50]
unique_list = remove_duplicates(initial_list)

print(f"Начальный список:  {initial_list}")
print(f"После удаления дублей:  {unique_list}")

print("#5")

numbers = []
squares = []
cubes = []

for i in range(1, 11):
    numbers.append(i)
    squares.append(i**2)
    cubes.append(i**3)

print(f"Числа:  {numbers}")
print(f"Квадраты:  {squares}")
print(f"Кубы :  {cubes}")

print("#6")

list1 = [10, 20, 30, 40, 50]
def reverse_list(list1):

  return list1[::-1]

reversed_list = reverse_list(initial_list)

print(f"Начальный список:  {initial_list}")
print(f"Список в обратном порядке:  {reversed_list}")

print("#7")

def remove_even_numbers(list1):

  odd_numbers = []
  for num in list1:
    if num % 2 != 0:
      odd_numbers.append(num)
  return odd_numbers

initial_list = [11, 22, 33, 44, 55]
odd_numbers_list = remove_even_numbers(initial_list)

print(f"Начальный список:  {initial_list}")
print(f"Список с нечетными числами:  {odd_numbers_list}")


print("#8")

def sum_lists(list1, list2):

  result = []
  for i in range(len(list1)):
    result.append(list1[i] + list2[i])
  return result

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
sum_list = sum_lists(list1, list2)

print(f"Первый список:  {list1}")
print(f"Второй список:  {list2}")
print(f"Результат сложения:  {sum_list}")

print("#9")

def dot_product(vector1, vector2):

  if len(vector1) != len(vector2):
    raise ValueError("Векторы должны иметь одинаковую размерность")

  dot_product = 0
  for i in range(len(vector1)):
    dot_product += vector1[i] * vector2[i]
  return dot_product

vector1 = [1, 2, 3, 4]
vector2 = [5, 6, 7, 8]
result = dot_product(vector1, vector2)

print(f"Первый вектор:  {vector1}")
print(f"Второй вектор:  {vector2}")
print(f"Скалярное произведение:  {result}")

print()
print("▶︎ •၊၊||၊|။||||‌၊|• 11:11")
print("(づᴗ _ᴗ)づ♡")
print("🦢")

input()

