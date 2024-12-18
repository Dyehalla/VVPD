# 4, 6, 8
from math import factorial


def count_sh(x):
    res = 0
    for n in range(1, 100, 2):
        res += (x ** n) / (factorial(n))
    return res


def count_ln_x_plus_one(x):
    res = 0
    k = 1
    for n in range(1, 100):
        res += (k ** n) / n
        k *= -1


def main():
    while True:
        print('1. Посчитать sh(x)')
        print('2. Посчитать ln(1 + x)')
        print('3. Посчитать arctg(x)')
        print('4. Выйти')
        act = input('Выберите действие: ')

        if act == '4':
            break

        if act not in ('1', '2', '3'):
            print('Неверный ввод')
            continue

        while True:
            try:
                x = int(input('Введите х: '))
                break
            except ValueError:
                print('Вводите числа')

        if act == '1':
            print('Результат:', count_sh(x))

        elif act == '2':
            print('Результат:', count_ln_x_plus_one(x))

        else:
            pass
