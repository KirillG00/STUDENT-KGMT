---
tags:
  - МоиЛекции
  - ЯзыкПрограммирования
  - Python
---
Модуль `random` управляет генерацией случайных чисел. Его основные функции:

- **random()**: генерирует случайное число от 0.0 до 1.0

- **randint()**: возвращает случайное число из определенного диапазона

- **randrange()**: возвращает случайное число из определенного набора чисел

- **shuffle()**: перемешивает список

- **choice()**: возвращает случайный элемент списка

Функция `random()` возвращает случайное число с плавающей точкой в промежутке от `0.0` до `1.0`. Если же нам необходимо число из большего диапазона, скажем от `0` до `100`, то мы можем соответственно умножить результат функции `random` на `100`.

```python
import random
 
number = random.random()  # значение от 0.0 до 1.0
print(number)
number = random.random() * 100  # значение от 0.0 до 100.0
print(number)
```

Функция `randint(min, max)` возвращает случайное целое число в промежутке между двумя значениями `min` и `max`.

```python
import random
 
number = random.randint(20, 35)  # значение от 20 до 35
print(number)
```

Функция `randrange()` возвращает случайное целое число из определенного набора чисел. Она имеет три формы:

- `randrange(stop)`: в качестве набора чисел, из которых происходит извлечение случайного значения, будет использоваться диапазон от 0 до числа `stop`
- `randrange(start, stop)`: набор чисел представляет диапазон от числа `start` до числа `stop`
- `randrange(start, stop, step)`: набор чисел представляет диапазон от числа `start` до числа `stop`, при этом каждое число в диапазоне отличается от предыдущего на шаг `step`

```python
import random
 
number = random.randrange(10)  # значение от 0 до 10 не включая
print(number)
number = random.randrange(2, 10)  # значение в диапазоне 2, 3, 4, 5, 6, 7, 8, 9
print(number)
number = random.randrange(2, 10, 2)  # значение в диапазоне 2, 4, 6, 8
print(number)
```

### Работа со списком

Для работы со списками в модуле `random` определены две функции: функция `shuffle()` перемешивает список случайным образом, а функция `choice()` возвращает один случайный элемент из списка:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)  
random_number = random.choice(numbers)
print(random_number)
```

### Все функции модуля random

- `random.seed([X], version=2)` - инициализация генератора случайных чисел. Если X не указан, используется системное время.
- `random.getstate()` - внутреннее состояние генератора.
- `random.setstate(state)` - восстанавливает внутреннее состояние генератора. Параметр state должен быть получен функцией `getstate()`.
- `random.getrandbits(N)` - возвращает N случайных бит.
- `random.randrange(start, stop, step)` - возвращает случайно выбранное число из последовательности.
- `random.randint(A, B)` - случайное целое число N, A ≤ N ≤ B.
- `random.choice(sequence)` - случайный элемент непустой последовательности.
- `random.shuffle(sequence, [rand])` - перемешивает последовательность (изменяется сама последовательность). Поэтому функция не работает для неизменяемых объектов.
- `random.sample(population, k)` - список длиной k из последовательности population.
- `random.random()` - случайное число от 0 до 1.
- `random.uniform(A, B)` - случайное число с плавающей точкой, A ≤ N ≤ B (или B ≤ N ≤ A).
- `random.triangular(low, high, mode)` - случайное число с плавающей точкой, low ≤ N ≤ high. Mode - распределение.
- `random.betavariate(alpha, beta)` - бета-распределение. alpha>0, beta>0. Возвращает от 0 до 1.
- `random.expovariate(lambd)` - экспоненциальное распределение. lambd равен 1/среднее желаемое. Lambd должен быть отличным от нуля. Возвращаемые значения от 0 до плюс бесконечности, если lambd положительно, и от минус бесконечности до 0, если lambd отрицательный.
- `random.gammavariate(alpha, beta)` - гамма-распределение. Условия на параметры alpha>0 и beta>0.
- `random.gauss(значение, стандартное отклонение)` - распределение Гаусса.
- `random.lognormvariate(mu, sigma)` - логарифм нормального распределения. Если взять натуральный логарифм этого распределения, то вы получите нормальное распределение со средним mu и стандартным отклонением sigma. mu может иметь любое значение, и sigma должна быть больше нуля.
- `random.normalvariate(mu, sigma)` - нормальное распределение. mu - среднее значение, sigma - стандартное отклонение.
- `random.vonmisesvariate(mu, kappa)` - mu - средний угол, выраженный в радианах от 0 до 2π, и kappa - параметр концентрации, который должен быть больше или равен нулю. Если каппа равна нулю, это распределение сводится к случайному углу в диапазоне от 0 до 2π.
- `random.paretovariate(alpha)` - распределение Парето.
- `random.weibullvariate(alpha, beta)` - распределение Вейбулла.

---
## Практическое задание

![[Задание. Игральные кубики]]

---
## Ссылки

1. [Модуль random](https://metanit.com/python/tutorial/6.1.php)

---

| [[Генерация байт-кода модулей\|Предыдущая лекция]] | [[Математические функции и модуль math\|Следующая лекция]] |
| -------------------------------------------------- | ---------------------------------------------------------- |
