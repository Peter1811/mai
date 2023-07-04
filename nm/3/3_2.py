import numpy as np
import matplotlib.pyplot as plt


def s(a, b, c, d, x):
    """
    Calculate s(x)
    """
    return a + b * x + c * x**2 + d * x**3


def tridiagonal_solve(A, b):
    """
    From lab 1-2
    Solves Ax=b, where A - tridiagonal matrix
    Returns x
    """
    n = len(A)
    # Step 1. Forward
    v = [0 for _ in range(n)]
    u = [0 for _ in range(n)]
    v[0] = A[0][1] / -A[0][0]
    u[0] = b[0] / A[0][0]
    for i in range(1, n-1):
        v[i] = A[i][i+1] / (-A[i][i] - A[i][i-1] * v[i-1])
        u[i] = (A[i][i-1] * u[i-1] - b[i]) / (-A[i][i] - A[i][i-1] * v[i-1])
    v[n-1] = 0
    u[n-1] = (A[n-1][n-2] * u[n-2] - b[n-1]) / (-A[n-1][n-1] - A[n-1][n-2] * v[n-2])

    # Step 2. Backward
    x = [0 for _ in range(n)]
    x[n-1] = u[n-1]
    for i in range(n-1, 0, -1):
        x[i-1] = v[i-1] * x[i] + u[i-1]
    return x


def spline_interpolation(x, y, x_test):
    """
    Get cubic spline interpolation s(x) of tabular function y = f(x)
    s(x) = a + b(x - x_{i-1}) + c(x - x_{i-1})^2 + d(x - x_{i-1})^3
    Returns:
        arrays of coefficients a, b, c, d for each interval,
        s(x_test)
    """
    if len(x) != len(y):
        print('Массивы должны быть одинаковой длины')
        raise BaseException
    n = len(x)

    # Step 1. Get c coefs
    h = [x[i] - x[i - 1] for i in range(1, len(x))]
    # tridiagonal matrix for calculating c:
    A = [[0 for _ in range(len(h)-1)] for _ in range(len(h)-1)]
    A[0][0] = 2 * (h[0] + h[1])
    A[0][1] = h[1]
    for i in range(1, len(A) - 1):
        A[i][i-1] = h[i-1]
        A[i][i] = 2 * (h[i-1] + h[i])
        A[i][i+1] = h[i]
    A[-1][-2] = h[-2]
    A[-1][-1] = 2 * (h[-2] + h[-1])

    m = [3.0 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1]) for i in range(1, len(h))]

    c = [0] + tridiagonal_solve(A, m)

    # Step 2. Get a coefs
    a = [y[i-1] for i in range(1, n)]

    # Step 3. Get b coefs
    b = [(y[i] - y[i-1]) / h[i-1] - (h[i-1] / 3.0) * (2.0 * c[i-1] + c[i]) for i in range(1, len(h))]
    b.append((y[-1] - y[-2]) / h[-1] - (2.0 * h[-1] * c[-1]) / 3.0)

    # Step 4. Get d coefs
    d = [(c[i] - c[i-1]) / (3.0 * h[i-1]) for i in range(1, len(h))]
    d.append(-c[-1] / (3.0 * h[-1]))

    # Calculate s(x_test)
    for interval in range(len(x)):
        if x[interval] <= x_test < x[interval+1]:
            i = interval
            break
    y_test = s(a[i], b[i], c[i], d[i], x_test - x[i])
    return a, b, c, d, y_test


def draw_plot(x_original, y_original, a, b, c, d, x_test, y_test):
    """
    Plot spline and original points
    """
    x, y = [], []
    for i in range(len(x_original) - 1):
        x1 = np.linspace(x_original[i], x_original[i + 1], 10)
        y1 = [s(a[i], b[i], c[i], d[i], j - x_original[i]) for j in x1]
        x.append(x1)
        y.append(y1)

    plt.scatter(x_original, y_original, color='r')
    plt.scatter(x_test, y_test, color='g')
    
    for i in range(len(x_original) - 1):
        plt.plot(x[i], y[i], color='b')

    plt.show()


if __name__ == '__main__':
    x = [0, 1.0, 2.0, 3.0, 5.0]
    y = [0, 0.45345, 0.52360, 0.0, -2.2672]
    x_test = 1.5

    a, b, c, d, y_test = spline_interpolation(x, y, x_test)
    for i in range(len(x) - 1):
        print(f'[{x[i]}; {x[i+1]})')
        print(f's(x) = {a[i]} + {b[i]}(x - {x[i]}) + {c[i]}(x - {x[i]})^2 + {d[i]}(x - {x[i]})^3')
    print(f's(x_test) = s({x_test}) = {y_test}')
    draw_plot(x, y, a, b, c, d, x_test, y_test)
