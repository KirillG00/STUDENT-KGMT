---
tags:
  - МоиЛекции
  - Инструмент
  - ЯзыкПрограммирования
  - Python
  - Практика
---
В прошлой теме было описано создание простейшего скрипта на языке **Python**. Для создания скрипта может использоваться любой текстовый редактор. Зачастую можно использовать **Notepad++**. Но есть и другой способ создания программ, который представляет использование различных интегрированных сред разработки или **IDE**.

> **Интегрированная среда разработки** (IDE) (от англ. Integrated Development Environment) — это программа, в которой разработчики пишут, проверяют, тестируют и запускают код, а также ведут большие проекты

IDE предоставляют нам текстовый редактор для набора кода, но в отличие от стандартных текстовых редакторов, IDE также обеспечивает полноценную подсветку синтаксиса, автодополнение или интеллектуальную подсказку кода, возможность тут же выполнить созданный скрипт, а также многое другое.

Для Python можно использовать различные среды разработки, но одной из самых популярных из них является среда **PyCharm**, созданная компанией JetBrains. Эта среда динамично развивается, постоянно обновляется и доступна для наиболее распространенных операционных систем - Windows, MacOS, Linux.

Правда, она имеет одно важное ограничение. А именно она доступна в двух основных вариантах: платный выпуск **Professional** и бесплатный **Community**. Многие базовые возможности доступны и в бесплатном выпуске Community. В то же время ряд возможностей, например, веб-разработка, доступны только в платном Professional.

В нашем случае воспользуемся бесплатным выпуском Community. Для этого перейдем на [страницу загрузки](https://www.jetbrains.com/pycharm/download/#section=windows) и загрузим установочный файл PyCharm Community.

![[Pasted image 20240516102152.png]]

После загрузки выполним его установку.

![[Pasted image 20240516102604.png]]

После завершения установки запустим программу. При первом запуске открывается начальное окно:

![[Pasted image 20240516102627.png]]

Создадим проект и для этого выберем пункт **New Project**.

Далее нам откроется окно для настройки проекта. В поле **Location** необходимо указать путь к проекту. В моем случае проект будет помещаться в папку **HelloApp**. Собственно название папки и будет названием проекта.

![[Pasted image 20240516102707.png]]

Кроме пути к проекту все остальные настройки оставим по умолчанию и нажмем на кнопку **Create** для создания проекта.

После этого будет создан пустой проект:

![[Pasted image 20240516102832.png]]

В центре среды будет открыт файл `main.py` с некоторым содержимым по умолчанию.

Теперь создадим простейшую программу. Для этого изменим код файла `main.py` следующим образом:

```python
name = input("Введите ваше имя: ")
print("Привет,", name)
```

Для запуска скрипта нажмем на зеленую стрелку в панели инструментов программы:

![[Pasted image 20240516102926.png]]

Также для запуска можно перейти в меню **Run** и там нажать на подпункт **Run 'main'**

После этого внизу IDE отобразится окно вывода, где надо будет ввести имя и где после этого будет выведено приветствие:

![[Pasted image 20240516103008.png]]

---
## Ссылки

1. [Notepad++](https://notepad-plus-plus.org/)
2. [Первая программа в PyCharm](https://metanit.com/python/tutorial/1.3.php)

---

| [[Установка Python\|Предыдущая лекция]] | [[Введение в написание программ\|Следующая лекция]] |
| --------------------------------------- | --------------------------------------------------- |
