# лаба 3 
## Условие

Напишите две функции для решения задач своего варианта - с использованием рекурсии и без.
![изображение](https://github.com/DarkSwordss89125/laba1/assets/160292757/497c24ed-a4f6-4d3e-9a27-a6aed9741b0e)


## Описание работы
# Условие для первой задачи
![изображение](https://github.com/DarkSwordss89125/laba1/assets/160292757/ff53a082-869e-4a56-be10-725262511371)

## Рекурсия
Импортируем библиотеку, объявляем функцию.

Прописываем если рекурсия равна единице, то возвращаем корень из трех.

Прописываем рекурсивный вызов функции и уменьшаем рекурсию на одну и возвращаем значение. 

В переменные записываем значения, выводим результат


## Без рекурсии
Объявляем функцию,создаем список

Проходимся через for каждое значение до i,

Возвращаем значение

Выводим
## РЕЗУЛЬТАТ
![изображение](https://github.com/DarkSwordss89125/laba1/assets/160292757/2c1bfbba-0551-4d47-8796-216b841bcbf6)

# ПЕРЕСЕЧЕНИЕ СПИСКОВ
# Условие
![изображение](https://github.com/DarkSwordss89125/laba1/assets/160292757/ab916557-cad9-4ca6-bb87-c89c6162f572)


## С рекурсией
Объявляем функцию со списком и индексами

Если индекс2=лист2, то мы проверили все элементы  и записали общие, тогда возвращает список

Если индекс1 равен длине list1, то сбрасываем индекс1 на 0 и увеличиваем индекс2+1

Если элемент list1[index1] совпадает с элементом list1[index1]
то значит они общие и добавляем в список, 

После всего функция вызывает рекурсивно себя, увеличивая index1 на один.

Выводим функци
## Без рекурсии
Объявляем функцию

Создаем общий список, куда будем складывать значения из двух списков

Перебираем все значение из первого списка

Перебираем все значения из второго списка

Если одинаковые, добавляем в общий список

Возвращаем значение

Выводим результат
## Результат:
![изображение](https://github.com/DarkSwordss89125/laba1/assets/160292757/43e42d73-061f-44aa-8360-48dc1f8d359f)

# Используемы материалы

1) [Recursion in Programming - Full Course - freeCodeCamp.org](https://www.youtube.com/watch?v=IJDJ0kBx2LM)
2) [🐍 Самоучитель по Python для начинающих. Часть 13: Рекурсивные функции - proglib.io](https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-13-rekursivnye-funkcii-2023-01-23)
3) [Как работает рекурсия – объяснение в блок-схемах и видео - Хабр](https://habr.com/ru/articles/337030/)



