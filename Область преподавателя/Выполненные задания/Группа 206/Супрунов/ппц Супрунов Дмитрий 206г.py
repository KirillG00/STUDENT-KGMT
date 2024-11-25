# Введение в написание программ
print("Программа для демонстрации основных концепций программирования")

# Переменные и типы данных
age = 30 # Целое число
height = 1.85 # Число с плавающей запятой
name = "Алекс" # Строка
is_student = True # Логическое значение

# Консольный ввод и вывод
user_name = input("Введите ваше имя: ")
print(f"Привет, {user_name}!")

# Арифметические операции с числами
x = 10
y = 5
sum_result = x + y
print(f"Сумма {x} и {y} равна {sum_result}")

# Поразрядные операции с числами
bitwise_and = x & 3
print(f"{x} & 3 = {bitwise_and}")

# Условные выражения и условная конструкция if
if age >= 18:
    print(f"{name} является взрослым.")
else:
    print(f"{name} является несовершеннолетним.")

# Циклы
for i in range(5):
    print(f"Итерация {i + 1}")

# Функции и параметры функции
def add_numbers(a, b):
    return a + b

result = add_numbers(x, y)
print(f"Результат сложения: {result}")

# Лямбда-выражение
multiply = lambda a, b: a * b
print(f"Произведение {x} и {y} равно {multiply(x, y)}")

# Преобразование типов
age_str = str(age)
print(f"Возраст в строковом формате: {age_str}")

# Область видимости переменных
def my_function():
    local_var = "Я локальная переменная"
    print(local_var)

my_function()
# print(local_var) # Это вызовет ошибку, так как local_var не доступна вне функции.

# Замыкание
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

closure = outer_function("Привет из замыкания!")
closure()

# Декораторы
def decorator_function(original_function):
    def wrapper_function():
        print("Обертка перед вызовом функции.")
        original_function()
        print("Обертка после вызова функции.")
    return wrapper_function

@decorator_function
def display():
    print("Функция отображения.")

display()

# Объектно-ориентированное программирование: классы и объекты
class Person:
    def __init__(self, name, age):
        self.name = name # Инкапсуляция атрибутов
        self.age = age

    @property
    def info(self): # Свойство для получения информации о человеке
        return f"{self.name}, {self.age} лет"

    def introduce(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет.")

person1 = Person("Алекс", 30)
person1.introduce()
print(person1.info)

# Наследование
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def introduce(self):
        super().introduce()
        print(f"Я изучаю {self.major}.")

student1 = Student("Иван", 20, "Программирование")
student1.introduce()