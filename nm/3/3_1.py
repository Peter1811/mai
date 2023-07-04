import math


def f(x):
    return x * math.cos(x)


def lagrange_interpolation(x, y, test_point):

    if len(x) != len(y):
        print('Длины массивов должны быть равны')
        raise BaseException
    
    res_str = 'L(x) ='
    value = 0 

    for i in range(len(x)):
        cur = ''  
        t = 1  
        den = 1
        for j in range(len(x)):
            if i == j:
                continue
            cur += f'(x-{x[j]:.2f})'
            t *= (test_point[0] - x[j])
            den *= (x[i] - x[j])
        if i:
            res_str += f' + {(y[i] / den):.2f}*' + cur
        else:
            res_str += f' {(y[i] / den):.2f}*' + cur
        value += y[i] * t / den

    return res_str, abs(value - test_point[1])


def newton_interpolation(x, y, test_point):

    if len(x) != len(y):
        print('Длины массивов должны быть равны')
        raise BaseException

    n = len(x)
    c = [y[i] for i in range(n)]
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            c[j] = float(c[j] - c[j - 1]) / float(x[j] - x[j - i])

    res_str = 'P(x) = '
    t = 0 

    cur = ''
    mult = 1
    for i in range(n):
        t += mult * c[i]
        if i == 0:
            res_str += f'{c[i]:.2f}'
        else:
            res_str += ' + ' + cur + '*' + f'{c[i]:.2f}'

        mult *= (test_point[0] - x[i])
        cur += f'(x-{x[i]:.2f})'

    return res_str, abs(t - test_point[1])


if __name__ == '__main__':
    x_a = [0, math.pi / 6, math.pi / 3, math.pi / 2]
    x_b = [0, math.pi / 6, 5 * math.pi / 12, math.pi / 2]
    y_a = [f(x) for x in x_a]
    y_b = [f(x) for x in x_b]

    x_test = math.pi / 4
    y_test = f(x_test)

    print('\nМногочлен Лагранжа\n')
    print('Многочлен в точках А')
    polynom, error = lagrange_interpolation(x_a, y_a, (x_test, y_test))
    print(polynom)
    print('Погрешность:', error)
    print()

    print('Многочлен в точках В')
    polynom, error = lagrange_interpolation(x_b, y_b, (x_test, y_test))
    print(polynom)
    print('Погрешность: ', error)
    print()

    print('Многочлен Ньютона\n')
    print('Многочлен в точках А')
    polynom, error = newton_interpolation(x_a, y_a, (x_test, y_test))
    print(polynom)
    print('Погрешность:', error)
    print()

    print('Многочлен в точках В')
    polynom, error = newton_interpolation(x_b, y_b, (x_test, y_test))
    print(polynom)
    print('Погрешность:', error)
