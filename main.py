# 4, 6, 8
from math import factorial


def count_sh(x):
    res = 0
    for n in range(1, 100, 2):
        res += (x ** n) / (factorial(n))
    return round(res, 3)


def count_ln_x_plus_one(x):
    res = 0
    k = 1
    for n in range(1, 1000):
        res += (x ** n) / n * k
        k *= -1
    return round(res, 3)


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
                x = float(input('Введите х: '))
                if act == '2' or act == '3':
                    if not (-1 < x <= 1):
                        print('x должен быть в диапозоне (-1;1]')
                break
            except ValueError:
                print('Вводите числа')

        if act == '1':
            print('Результат:', count_sh(x))

        elif act == '2':
            print('Результат:', count_ln_x_plus_one(x))

        else:
            pass


if __name__ == '__main__':
    main()