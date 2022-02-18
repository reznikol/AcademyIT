# Решение квадратного уравнения
try:
    a = input('Введите a: ')
    b = input('Введите b: ')
    c = input('Введите c: ')
    if ',' in a or b or c:
        a = float(a.replace(',', '.'))
        b = float(b.replace(',', '.'))
        c = float(c.replace(',', '.'))
    if a != 0:
        D = b ** 2 - 4 * a * c
        sqrtD = D ** 0.5
        if D == 0:
            x = (-b + sqrtD) / (2 * a)
            print('Уравнение имеет один корень:', format(x, '.5f'))
        elif D < 0:
            print('Уравленение не имеет корней.')
        else:
            x1 = (-b + sqrtD) / (2 * a)
            x2 = (-b - sqrtD) / (2 * a)
            print(f'Уравнение имеет два корня:', format(x1, '.5f'), 'и', format(x2, '.5f'))
    else:
        print('Это не квадратное уравнение')
except ValueError:
    print('ОШИБКА: вводимые данные должны быть числами!')
