# Необходимо написать следующую функцию генератор Фибоначчи и проверить его работу. 
# Напишите функцию генератор nfib, которая имеет один аргумент, максимальное количество чисел Фибоначчи, которое она может выдать:
# • первое число Фибоначчи равно 1
# • второе число Фибоначчи равно 1
# • третье число Фибоначчи равно 2 или сумме двух предыдущих = 1 + 1
# • четвёртое число Фибоначчи равно 3 или сумме двух предыдущих = 2 + 1
# • пятое число Фибоначчи равно 5 или сумме двух предыдущих = 3 + 2
# • 8 = 5 + 3
# • и т.д.
# Необходимо протестировать функцию генератор nfib чисел Фибоначчи следующими способами с выводом результатов на экран:
# • создание списка из 20 чисел Фибоначчи с помощью функции list()
# • создание списка из 20 чисел Фибоначчи с помощью генератора списка
# • создание списка из 20 чисел Фибоначчи с помощью цикла for
# • создание множества из 20 чисел Фибоначчи с помощью генератора множества

# -----------------------------------------------------------------------------------------------------

#!usr/bin/env/python3
# -*- coding: utf-8 -*-

# Функция генератор nfib, с аргументом, который принимает максимальное количество выводов чисел Фибоначчи
def nfib(n):
    f1, f2 = 1, 1
    for i in range(n):
        yield f1
        f1, f2 = f2, f1 + f2
print(nfib(20))

# Проверки
print(list(nfib(20))) # Создается список из 20 чисел Фибоначчи с помощью функции list()

data = {i for i in nfib(20)} # Создается список из 20 чисел Фибоначчи с помощью генератора множеств
print(data)

data = [i for i in nfib(20)] # Создается список из 20 чисел Фибоначчи с помощью генератора списка
print(data)

s = []
for i in nfib(20): # Создается список из 20 чисел Фибоначчи с помощью цикла for
    s.append(i)
print(s, end=' ')

print()
for i in nfib(20): # Создается простой список из 20 чисел Фибоначчи с помощью цикла for типа int
    print(i, end=' ')
