# Необходимо написать программу, выполняющую сортировку методом пузырька и проверить её работу. 
# Программа должна сделать следующие условия:
# • Попросить пользователя ввести количество чисел для сортировки от 20 до 1000.
# • Ввод числа необходимо оформить в виде функции nask, которая имеет следующие параметры (аргументы функции nask):
#    - oamin, минимальное количество точек, которое может ввести пользователь. Если аргумент функции не указан, значение по умолчанию равно 20.
#    - Проверить, что аргумент функции amin больше 20. Если меньше 20, то установить его равным 20.
#    - amax, максимальное количество точек, которое может ввести пользователь. Если аргумент функции не указан, значение по умолчанию равно 1000.
#    - Проверить, что аргумент функции amax меньше 1000. Если он больше 1000, то установить его равным 1000.
#    - Функция nask должна попросить ввести количество точек для сортировки.
# • Получение информации от пользователя:
#    - Функция nask должна попросить ввести количество для сортировки, написав минимальное и максимально возможное значение.
# • Проверка ввода пользователя:
#    - Если пользователь вводит не целое число, то функция должна попросить пользователя повторить ввод.
#    - Если пользователь вводит числа меньше amin, то программа должна сообщить об этом пользователю и повторить ввод.
#    - Если пользователь вводит числа больше amax, то программа должна сообщить об этом пользователю и повторить ввод.
# • Функция nask должна вернуть целое число точек для сортировки, которое ввёл пользователь..
# • Сформировать список со случайными целыми числами от 10000 до 99999.
# • Длина списка равна числу, которое мы спросили у пользователя с помощью функции nask.
# • Создать функцию сортировки bub_sort.
# • Выполнить сортировку данного списка методом пузырька с помощью функции bub_sort:
#    - Аргументы функции – список, который необходимо отсортировать
#    - Функция ничего не возвращает и сортирует список на месте.
# • Программа должна напечатать:
#    - Количество чисел в списке.
#    - Процессорное время, которое было затрачено на сортировку.
#    - Вывод процессорного времени необходимо напечатать в секундах с точностью 3 знака после запятой.
#    - Сумму 10 максимальных чисел отсортированного списка.
#    - Сумму 10 минимальных чисел отсортированного списка.
# Программа не должна выдавать программных ошибок, при неправильном вводе пользователя, за исключением сигналов прерывание программы Ctrl+C.

# -------------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
from time import process_time


# Функция, которая спрашивает число у пользователя и возвращает целое число
def nask(*, amin = 20, amax = 1000):
    if amin < 20:
        amin = 20
    if amax > 1000:
        amax = 1000
    # Обработка некорректного ввода пользователем
    while True:
        a = input(f'Введите целое число для сортировки от {amin} до {amax} включительно: ')
        # Если пользователь ввёл пустую стоку, указывается агрумент по умолчанию - максимум
        if not a.strip():
            a = amax
        try:
            a = int(a)
            # Сообщение пользователю о превышении минимума и максимума
            if a < amin:
                print(f'Введите целое число больше {amin}. Вы ввели: {a}')
            elif a > amax:
                print(f'Введите целое число меньше {amax}. Вы ввели: {a}')
            # Если число указано в предельных границах, то прерывание бесконечного цикла
            else:
                break
        # Если оператор a = int(a) вызвал ошибку ValueError
        except ValueError:
            # Вывод сообщения пользователю
            print(f'Вы ввели недопустимое значение "{a}", нужно ввести целое число. Повторите ввод!')
        # Выполняем цикл ещё раз
    return a

n = nask(amin = 20, amax = 1000)

# Создание списка случайных чисел от 10000 до 99999
spis = [randint(10000, 99999) for _ in range(n)] 


# Функция сортировки методом пузырька
def bub_sort(s):
    for i in range(len(s) - 1):
        for j in range(len(s) - i - 1):
             if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
    return s

print(f'Количество чисел в списке: {len(bub_sort(spis))}')

# Определение процессорного времени, затраченного на выполнение сортировки
t0 = process_time()
bub_sort(spis)
t1 = process_time() - t0

print(f'Время сортировки списка методом пузырька составило: {t1:2.3f} сек.') # точность 3 значка после запятой

print(f'Сумма минимальных 10 значений списка составит: {sum(bub_sort(spis[:10]))}')
print(f'Сумма максимальных 10 значений списка составит: {sum(bub_sort(spis[-10:]))}')
