#!usr/bin/env/python3
# -*- coding: utf-8 -*-

txt = """Анализ текста по буквам. Практическое задание №2

Написать программу на Python для анализа данного текста, который сохранён в переменной txt по буквам. Программа на Python должна проанализировать данный текст и вывести, или, как некоторые Users говорят, напечатать следующую информацию. Необходимо вывести: 

# Общее количество букв в данном тексте
# Общее количество слов в данном тексте. Словом, считаются любые символы, разделённые пробелами или переходом на следующую строку.
# Подсчитать, каких букв и сколько встречается в тексте
# Вывести их на печать
# 1) в алфавитном порядке
# 2) в порядке убывания частоты
# Регистр букв значения не имеет! Например, в тексте 'Aa' буква 'а'
# встречается 2 раза
# В структуре данных, которую вы выберете для хранения информации
# во время работы программы, НЕ ХРАНИТЬ буквы, которые не встретились"""

# ***********************************
txt = list(txt.split())

# Функция подсчета количество букв и слов в тексте
def words_letters_calculate(text):
    words = len(text)
    letters = 0

    for l in text:
        l = l.strip('[.:#!,)№12\']')
        letters += len(l) 
    return letters, words

# Анализ текста по символам
simbols = dict()

for line in txt:
    line = line.strip('[.:#!,)№12\']').lower()

    for letter in line:
        if letter in simbols: 
            simbols[letter] += 1
        else:
           simbols[letter] = 1

# Сортировки                
list_simbols1 = list(simbols.items())
list_simbols1.sort()

list_simbols2 = [(n, l) for l, n in simbols.items()]
list_simbols2.sort(reverse=True)

# Печать количества букв и слов              
nl, nw = words_letters_calculate(txt)
print(f'Общее количество букв в данном тексте: {nl} \nОбщее количество слов в данном тексте: {nw}\n')

# Печать по алфавиту
print('Буквы в тексте в алфавитном порядке\n')
for b, n in list_simbols1:
    print(f'Буква "{b}" встречается в тексте: {n:2} раз')

# Печать в порядке убывания частоты 
print('\nБуквы в тексте в порядке убывания частоты\n')
for n, b in list_simbols2:
    print(f'Буква "{b}" встречается в тексте: {n:2} раз')
    
# ***********************************
print('END')
