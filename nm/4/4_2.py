import math
from math import exp
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable


def runge_kutta_method(
        f: Callable[[float, float, float], float], 
        g: Callable[[float, float, float], float], 
        y0: float, 
        z0: float, 
        interval: tuple[float],
        h: float
    ) -> tuple[list[float]]:
    l: int = interval[0]
    r: int = interval[1]
    x: list[float] = [float(i) for i in np.arange(l, r + h, h)]
    y: list[float] = [y0, ]
    z: list[float] = [z0, ]
    for i in range(len(x) - 1):
        K1: float = h * g(x[i], y[i], z[i])
        L1: float = h * f(x[i], y[i], z[i])
        K2: float = h * g(x[i] + 0.5 * h, y[i] + 0.5 * K1, z[i] + 0.5 * L1)
        L2: float = h * f(x[i] + 0.5 * h, y[i] + 0.5 * K1, z[i] + 0.5 * L1)
        K3: float = h * g(x[i] + 0.5 * h, y[i] + 0.5 * K2, z[i] + 0.5 * L2)
        L3: float = h * f(x[i] + 0.5 * h, y[i] + 0.5 * K2, z[i] + 0.5 * L2)
        K4: float = h * g(x[i] + 0.5 * h, y[i] + 0.5 * K3, z[i] + 0.5 * L3)
        L4: float = h * f(x[i] + 0.5 * h, y[i] + 0.5 * K3, z[i] + 0.5 * L3)
        delta_y = (K1 + 2 * K2 + 2 * K3 + K4) / 6
        delta_z = (L1 + 2 * L2 + 2 * L3 + L4) / 6
        y.append(y[i] + delta_y)
        z.append(z[i] + delta_z)

    return (x, y, z)


def tridiagonal_solve(A: list[list[float]], b: list[float]) -> list[float]:
    n: int = len(A)
    v: list[float] = [0 for _ in range(n)]
    u: list[float] = [0 for _ in range(n)]
    v[0] = A[0][1] / -A[0][0]
    u[0] = b[0] / A[0][0]
    for i in range(1, n-1):
        if not(abs(A[i][i]) > abs(A[i][i - 1]) + abs(A[i][i + 1])):
            print("Выполняется условие на преобладание диагональных элементов!")

        v[i] = A[i][i+1] / (-A[i][i] - A[i][i-1] * v[i-1])
        u[i] = (A[i][i-1] * u[i-1] - b[i]) / (-A[i][i] - A[i][i-1] * v[i-1])
    v[n-1] = 0
    u[n-1] = (A[n-1][n-2] * u[n-2] - b[n-1]) / (-A[n-1][n-1] - A[n-1][n-2] * v[n-2])

    x: list[float] = [0 for _ in range(n)]
    x[n-1] = u[n-1]
    for i in range(n-1, 0, -1):
        x[i-1] = v[i-1] * x[i] + u[i-1]
    return x


def f(x: float, y: float, z: float) -> float:
    return math.tan(x) * z - 2 * y


def g(x: float, y: float, z: float) -> float:
    return z


# Functions for finite difference method
# y'' + p_fd(x)y' + q_fd(x)y = f_fd(x)

def p_fd(x: float) -> float:
    return -math.tan(x)


def q_fd(x: float) -> float:
    return 2


def f_fd(x: float) -> float:
    return 0


def exact_solution(x: float) -> float:
    return math.sin(x) + 2 - math.sin(x) * math.log((1 + math.sin(x)) / (1 - math.sin(x)))


def shooting_method(
    f: Callable[[float, float, float], float],
    g: Callable[[float, float, float], float],
    y0: list[float], 
    yn: list[float], 
    interval: tuple[float],
    h: float, 
    eps: float
    ) -> tuple[list[float], list[float], float]:
    
    n_prev: float = 1.0
    n: float = 0.8
    iterations: float = 0
    while True:
        iterations += 1
        x_prev, y_prev, z_prev = runge_kutta_method(f, g, y0, n_prev, interval, h)
        x, y, z = runge_kutta_method(f, g, y0, n, interval, h)
        if abs(y[-1] - yn) < eps:
            break
        n_prev, n = n, n - (y[-1] - yn) * (n - n_prev) / ((y[-1] - yn) - (y_prev[-1] - yn))
    return x, y, iterations


def finite_difference_method(p, q, f, y0, yn, interval, h):
    A = []
    B = []
    rows = []
    a, b = interval
    x = np.arange(a, b + h, h)
    n = len(x)

    # Creating tridiagonal matrix
    for i in range(n):
        if i == 0:
            rows.append(1)
        else:
            rows.append(0)
    A.append(rows)
    B.append(y0)

    for i in range(1, n - 1):
        rows = []
        B.append(f(x[i]))
        for j in range(n):
            if j == i - 1:
                rows.append(1 / h ** 2 - p(x[i]) / (2 * h))
            elif j == i:
                rows.append(-2 / h ** 2 + q(x[i]))
            elif j == i + 1:
                rows.append(1 / h ** 2 + p(x[i]) / (2 * h))
            else:
                rows.append(0)
        A.append(rows)

    rows = []
    B.append(yn)
    for i in range(n):
        if i == n - 1:
            rows.append(1)
        else:
            rows.append(0)

    A.append(rows)
    print("a = ", A, "b = ", B)
    y = tridiagonal_solve(A, B)
    print("y = ", y)
    return x, y


def runge_romberg_richardson_method(
        h1: float,
        h2: float,
        y1: list[float],
        y2: list[float],
        p: float
    ) -> list[float]:
    if h1 != 2 * h2:
        print('Ошибка, h1 должен быть в два раза больше h2')
        return -1

    result: list[float] = []
    for i in range(len(y1)):
        result.append(y2[2 * i] + (y2[2 * i] - y1[i]) / (2 ** p - 1))
    
    return result


def mean_absolute_error(func: list[float], exact_func: list[float]) -> float:
    res = 0
    for i in range(len(func)):
        res += abs(func[i] - exact_func[i])
    return res / len(func)


if __name__ == '__main__':
    y0 = 2
    y1 = 1.955
    interval = (0.0, 0.5)
    h = 0.1
    eps = 0.001
    
    x_shooting2, y_shooting2, iters_shooting2 = shooting_method(f, g, y0, y1, interval, h / 0.9, eps)
    plt.plot(x_shooting2, y_shooting2, label=f'Итерация 1')
    x_exact = [i for i in np.arange(interval[0], interval[1] + h, h)]
    x_exact2 = [i for i in np.arange(interval[0], interval[1] + h / 2, h / 2)]
    y_exact = [exact_solution(x_i) for x_i in x_exact]
    y_exact2 = [exact_solution(x_i) for x_i in x_exact2]
    plt.plot(x_exact, y_exact, label=f'Итерация 2')
    x_shooting3, y_shooting3, iters_shooting3 = shooting_method(f, g, y0, y1, interval, h / 0.75, eps)
    plt.plot(x_shooting3, y_shooting3, label=f'Итерация 3')
    x_shooting4, y_shooting4, iters_shooting4 = shooting_method(f, g, y0, y1, interval, h / 0.95, eps)
    plt.plot(x_shooting4, y_shooting4, label=f'Итерация 4')
    x_shooting5, y_shooting5, iters_shooting5 = shooting_method(f, g, y0, y1, interval, h / 0.99, eps)
    plt.plot(x_shooting5, y_shooting5, label=f'Итерация 5')
    real_x, real_y, real_iters = shooting_method(f, g, y0, y1, interval, h / 10, eps)
    plt.plot(real_x, real_y, label=f'Точная функция')


    x_fd, y_fd = finite_difference_method(p_fd, q_fd, f_fd, y0, y1, interval, h)
    plt.plot(x_fd, y_fd, label=f'Метод конечных разностей, шаг = {h}')
    x_fd2, y_fd2 = finite_difference_method(p_fd, q_fd, f_fd, y0, y1, interval, h / 2)
    plt.plot(x_fd2, y_fd2, label=f'Метод конечных разностей, шаг = {h / 2}')

    # print('\nПогрешность численного решения с помощью метода Рунге-Ромберга:')
    # runge_romberg_shooting: list[float] = runge_romberg_richardson_method(h, h / 2, x_shooting5, x_shooting3, 1)
    # runge_romberg_fd: list[float] = runge_romberg_richardson_method(h, h / 2, x_fd, x_fd2, 4)
    # print('Метод стрельбы: ', *runge_romberg_shooting, end='\n\n')
    # print('Метод Рунге-Кутты: ', *runge_romberg_fd, end='\n\n')

    print('Отклонение от точного решения:')
    print('Метод стрельбы на 4 итерации: ', mean_absolute_error(x_shooting5, y_shooting5), end='\n\n')
    print('Метод конечных разностей с шагом h = {h}: ', mean_absolute_error(x_fd, y_fd), end='\n\n')
    

    plt.legend()
    plt.show()