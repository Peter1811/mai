import math

def f(x):
    return x**2 / (x**4 + 256)

eps = 0.001


def integrate_rectangle_method(f, l, r, h):
    result = 0
    cur_x = l
    while cur_x < r:
        result += f((cur_x + cur_x + h) / 2)
        cur_x += h
    result = h * result
    return result


def integrate_trapeze_method(f, l, r, h):
    result = 0
    cur_x = l
    while cur_x < r:
        result += (f(cur_x + h) + f(cur_x))
        cur_x += h
    result = h * result
    return result * 0.5

def integrate_simpson_method(f, l, r, h):
    result = 0
    cur_x = l + h
    i = 0
    while cur_x < r:
        i += 1
        result += f(cur_x - h) + 4*f(cur_x) + f(cur_x + h)
        cur_x += 2 * h

    if i % 2:
        print('Error with step selection, changing step')
        result = 0
        h -= eps
        cur_x = l + h
        while cur_x < r:
            result += f(cur_x - h) + 4*f(cur_x) + f(cur_x + h)
            cur_x += 2 * h
    
    return result * h / 3


def runge_romberg_method(h1, h2, integral1, integral2, p):
    if h2 > h1:
        return integral1 + (integral1 - integral2) / ((h2 / h1) ** p - 1)
    else:
        return integral2 + (integral2 - integral1) / ((h1 / h2) ** p - 1)


if __name__ == '__main__':
    l, r = 0, 2  # interval of integrating
    h1, h2 = 0.5, 0.25  # steps

    print('\nRectangle method')
    int_rectangle_h1 = integrate_rectangle_method(f, l, r, h1)
    int_rectangle_h2 = integrate_rectangle_method(f, l, r, h2)
    print(f'Step = {h1}: integral = {int_rectangle_h1}')
    print(f'Step = {h2}: integral = {int_rectangle_h2}')

    print('\nTrapeze method')
    int_trapeze_h1 = integrate_trapeze_method(f, l, r, h1)
    int_trapeze_h2 = integrate_trapeze_method(f, l, r, h2)
    print(f'Step = {h1}: integral = {int_trapeze_h1}')
    print(f'Step = {h2}: integral = {int_trapeze_h2}')

    print('\nSimpson method')
    int_simpson_h1 = integrate_simpson_method(f, l, r, h1)
    int_simpson_h2 = integrate_simpson_method(f, l, r, h2)
    if int_simpson_h1 != -1:
        print(f'Step = {h1}: integral = {int_simpson_h1}')
    
    if int_simpson_h2 != -1:
        print(f'Step = {h2}: integral = {int_simpson_h2}')

    print('\nRunge Rombert method')
    print(f'More accurate integral by rectangle method = {runge_romberg_method(h1, h2, int_rectangle_h1, int_rectangle_h2, 3)}')
    print(f'More accurate integral by trapeze method = {runge_romberg_method(h1, h2, int_trapeze_h1, int_trapeze_h2, 3)}')
    print(f'More accurate integral by Simpson method = {runge_romberg_method(h1, h2, int_simpson_h1, int_simpson_h2, 3)}')
