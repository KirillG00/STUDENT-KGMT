---
tags:
  - МоиЛекции
  - ЯзыкПрограммирования
  - Python
---
> **Python** – это популярный высокоуровневый язык программирования, который предназначен для создания приложений различных типов, такие как веб-приложения, и игры, и настольные программы, и работа с базами данных. 

Довольно большое распространение питон получил в области машинного обучения и исследований искусственного интеллекта.

Впервые язык Python был анонсирован в 1991 году голландским разработчиком *Гвидо Ван Россумом*. С тех пор данный язык проделал большой путь развития. В 2000 году была издана версия 2.0, а в 2008 году – версия 3.0. Несмотря на такие большие промежутки между версиями постоянно выходят подверсии. Так, текущей актуальной версией на момент написания данного материала является 3.12, которая вышла в октябре 2023 года.

Основная причина выбора языка программирования Python заключается в том, что этот язык является языком **полного спектра**. Это значит что **Python** является одновременно очень мощным языком программирования со множеством возможностей и инструментов, но при этом не мешает начинать с основ и осваивать расширенные возможности по мере роста потребностей вашего приложения. Вот другие особенности языка Python:

- **Скриптовый язык**. Код программ определяется в виде скриптов;
- **Поддержка самых различных парадигм программирования**, в том числе объектно-ориентированной и функциональной парадигм;
- **[[Интерпретация]] программ**. Для работы со скриптами необходим [[Интерпретатор|интерпретатор]], который запускает и выполняет скрипт.


Выполнение программы на Python выглядит следующим образом, пошагово: 

1. Сначала мы пишем в текстовом редакторе скрипт с набором выражений на данном языке программирования;
2. Передаем этот скрипт на выполнение интерпретатору;
3. [[Интерпретатор]] транслирует код в промежуточный байт-код, а затем виртуальная машина переводит полученный байт-код в набор инструкций, которые выполняются операционной системой.

Здесь стоит отметить, что хотя формально трансляция интерпретатором исходного кода в байт-код и перевод байт-кода виртуальной машиной в набор машинных команд представляют два разных процесса, но фактически они объединены в самом интерпретаторе.

![Выполнение программы на Python](https://metanit.com/python/tutorial/pics/1.9.png)

- **Портативность и платформонезависимость.** Не имеет значения, какая у нас операционная система – Windows, Mac OS, Linux, нам достаточно написать скрипт, который будет запускаться на всех этих ОС при наличии интерпретатора;
- Автоматическое управление памяти;
- Динамическая типизация.

**Python** – очень простой язык программирования, он имеет лаконичный и в то же время довольно простой и понятный синтаксис. Соответственно его легко изучать, и собственно это одна из причин, по которой он является одним из самых популярных языков программирования именно для обучения. В частности, в 2014 году он был признан самым популярным языком программирования для обучения в США.

Python также популярен не только в сфере обучения, но в написании конкретных программ в том числе коммерческого характера. В немалой степени поэтому для этого языка написано множество библиотек, которые мы можем использовать.

Кроме того, у данного языка программирования очень большое сообщество программистов, в интернете можно найти по данному языку множество полезных материалов, примеров, получить квалифицированную помощь специалистов.

### Пакеты и библиотеки

[[Интерпретатор]] Python сопровождается достаточным функционалом, который позволяет создавать приложения на этом языке. Тем не менее этого функционала может оказаться недостаточно для ряда задач. Но в виду большого сообщества разработчиков на этом языке по всему миру также имеется большая экосистема различных пакетов и библиотек, которые можно использовать для различных целей. Если хотите более подробно разобраться со стандартными библиотеками языка Python, то рекомендую смотреть в [разделе языка Python](https://metanit.com/python/) на сайте [METANIT.COM](https://metanit.com/), где будут рассмотрены некоторые из этих библиотек. Вот основные из них:

Для создания **графических приложений**:

- [Tkinter](https://metanit.com/python/tkinter)
- PyQt / PySide
- wxPython
- DearPyGui
- EasyGUI

---
Для создания **мобильных приложений**:

- [[Введение в Kivy|Kivy]]
- Toga

---
Для создания **веб-приложений**:

- [Django](https://metanit.com/python/django)
- Flask
- [FastAPI](https://metanit.com/python/fastapi)
- Pylons
- Bottle
- CherryPy
- TurboGears
- Nagare

---
Для **автоматизации процессов**:

- Selenium (для тестирования веб-приложений)
- Flask
- FastAPI
- Pylons
- Bottle
- CherryPy
- TurboGears
- Nagare
- robotframework
- pywinauto
- Lettuce
- Behave
- Requests

---
Для **работы с различными типами файлов**:

- OpenPyXL (Excel)
- lxml (XML)
- ReportLab / borb (PDF)
- pdfrw / PyPDF2 (PDF)
- Pandas (CSV и Excel)

---
Для **машинного обучения, искусственного интеллекта, Data Science**:

- Pandas
- SciPy
- PyTorch
- Matplotlib
- Theano
- Tensorflow
- OpenCV
- Scikit-Learn
- Keras
- NumPy

---
Для **визуализации**:

- Matplotlib
- Seaborn
- Plotly
- Bokeh
- Altair
- HoloViews

---
## Ссылки

1. [Введение в Python](https://metanit.com/python/tutorial/1.1.php)
2. [[Знакомство с Python.pdf|Знакомство с Python, cтр. 15 - 20]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/MunPNYumw6M?si=l5REn6VbDAre7wWM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

| [[Установка Python\|Следующая лекция]] |
| -------------------------------------- |
