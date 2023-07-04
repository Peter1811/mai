def df(x_test, x, y):
    """
    Calculate first derivative of tabular function f(x) = y at point=x_test
    Returns df(x_test)
    """
    assert len(x) == len(y)
    for interval in range(len(x)):
        if x[interval] <= x_test < x[interval+1]:
            i = interval
            break

    a1 = (y[i+1] - y[i]) / (x[i+1] - x[i])
    a2 = ((y[i+2] - y[i+1]) / (x[i+2] - x[i+1]) - a1) / (x[i+2] - x[i]) * (2*x_test - x[i] - x[i+1])
    return a1 + a2


def d2f(x_test, x, y):
    """
    Calculate second derivative of tabular function f(x) = y at point=x_test
    Returns d2f(x_test)
    """
    assert len(x) == len(y)
    for interval in range(len(x)):
        if x[interval] <= x_test < x[interval+1]:
            i = interval
            break

    num = (y[i+2] - y[i+1]) / (x[i+2] - x[i+1]) - (y[i+1] - y[i]) / (x[i+1] - x[i])
    return 2 * num / (x[i+2] - x[i])


if __name__ == '__main__':
    x = [0.0, 2.0, 4.0, 6.0, 8.0]
    y = [0.0, 0.048856, 0.23869, 0.65596, 1.4243]
    x_test = 0.4

    print('First derivative')
    print(f'df({x_test}) = {df(x_test, x, y)}')

    print('Second derivative')
    print(f'd2f({x_test}) = {d2f(x_test, x, y)}')
