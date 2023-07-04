from typing import Callable
import matplotlib.pyplot as plt
import numpy as np

# (x * x - 1)y'' - 2xy' + 2y = 0
# (x * x - 1)z' - 2xz + 2y = 0

def f(x: float, y: float, z: float) -> float:
    return (2 * x * z - 2 * y) / (x * x - 1)

def g(x: float, y: float, z: float) -> float:
    return z

def exact_func(x: float) -> float:
    return x * x + x + 1

def eiler_method(
        f: Callable[[float, float, float], float], 
        g: Callable[[float, float, float], float], 
        h: float, 
        y0: float, 
        z0: float, 
        interval: tuple[float]
    ) -> tuple[list[float]]:

    l: int = interval[0]
    r: int = interval[1]
    x: list[float] = [float(_) for _ in np.arange(l, r + h, h)]
    y: list[float] = [y0, ]
    z: float = z0
    for i in range(len(x) - 1):
        z += h * f(x[i], y[i], z)
        y.append(y[i] + h * g(x[i], y[i], z))

    return (x, y)


def runge_kutt_method(
        f: Callable[[float, float, float], float], 
        g: Callable[[float, float, float], float], 
        h: float, 
        y0: float, 
        z0: float, 
        interval: tuple[float]
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
        K4: float = h * g(x[i] + h, y[i] + K3, z[i] + L3)
        L4: float = h * f(x[i] + h, y[i] + K3, z[i] + L3)
        delta_y = (K1 + 2 * K2 + 2 * K3 + K4) / 6
        delta_z = (L1 + 2 * L2 + 2 * L3 + L4) / 6
        y.append(y[i] + delta_y)
        z.append(z[i] + delta_z)

    return (x, y, z)


def adams_method(
        f: Callable[[float, float, float], float], 
        g: Callable[[float, float, float], float], 
        h: float, 
        y0: float, 
        z0: float, 
        interval: tuple[float]
    ) -> tuple[list[float]]:
    params: tuple[list[float]] = runge_kutt_method(f, g, h, y0, z0, interval)
    x: list[float] = params[0]
    y: list[float] = params[1][:4]
    z: list[float] = params[2][:4]
    for i in range(3, len(x) - 1):
        z_i = z[i] + h * (55 * f(x[i], y[i], z[i]) -
                          59 * f(x[i - 1], y[i - 1], z[i - 1]) + 
                          37 * f(x[i - 2], y[i - 2], z[i - 2]) - 
                          9 * f(x[i - 3], y[i - 3], z[i - 3])) / 24
        z.append(z_i)
        y_i = y[i] + h * (55 * g(x[i], y[i], z[i]) -
                          59 * g(x[i - 1], y[i - 1], z[i - 1]) + 
                          37 * g(x[i - 2], y[i - 2], z[i - 2]) - 
                          9 * g(x[i - 3], y[i - 3], z[i - 3])) / 24
        y.append(y_i)

    return (x, y)

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
    y0: float = 7.0
    dy0: float = 5.0
    interval: tuple[int] = (2, 3)
    h: float = 0.1

    eiler_h: tuple[list[float]] = eiler_method(f, g, h, y0, dy0, interval)
    x_eiler_h: list[float] = eiler_h[0]
    y_eiler_h: list[float] = eiler_h[1]
    plt.plot(x_eiler_h, y_eiler_h, label=f'Метод Эйлера, шаг = {h}')

    eiler_h_div_2: tuple[list[float]] = eiler_method(f, g, h / 2, y0, dy0, interval)
    x_eiler_h_div_2: list[float] = eiler_h_div_2[0]
    y_eiler_h_div_2: list[float] = eiler_h_div_2[1]
    # plt.plot(x_eiler_h_div_2, y_eiler_h_div_2, label=f'Метод Эйлера, шаг = {h / 2}')

    runge_kutt_h: tuple[list[float]] = runge_kutt_method(f, g, h, y0, dy0, interval)
    x_runge_kutt_h: list[float] = runge_kutt_h[0]
    y_runge_kutt_h: list[float] = runge_kutt_h[1]
    plt.plot(x_runge_kutt_h, y_runge_kutt_h, label=f'Метод Рунге-Кутта, шаг = {h}')

    runge_kutt_h_div_2: tuple[list[float]] = runge_kutt_method(f, g, h / 2, y0, dy0, interval)
    x_runge_kutt_h_div_2: list[float] = runge_kutt_h_div_2[0]
    y_runge_kutt_h_div_2: list[float] = runge_kutt_h_div_2[1]
    # plt.plot(x_runge_kutt_h, y_runge_kutt_h, label=f'Метод Рунге-Кутта, шаг = {h / 2}')

    adams_h: tuple[list[float]] = adams_method(f, g, h, y0, dy0, interval)
    x_adams_h: list[float] = adams_h[0]
    y_adams_h: list[float] = adams_h[1]
    plt.plot(x_adams_h, y_adams_h, label=f'Метод Адамса, шагом = {h}')

    adams_h_div_2: tuple[list[float]] = adams_method(f, g, h / 2, y0, dy0, interval)
    x_adams_h_div_2: list[float] = adams_h_div_2[0]
    y_adams_h_div_2: list[float] = adams_h_div_2[1]
    # plt.plot(x_adams_h_div_2, y_adams_h_div_2, label=f'Метод Адамса, шагом = {h / 2}')

    x_exact: list[float] = [_ for _ in np.arange(interval[0], interval[1] + h, h)]
    y_exact: list[float] = [exact_func(_) for _ in x_exact]
    plt.plot(x_exact, y_exact, label='Точное решение')

    print('\nУточнение численного решения с помощью метода Рунге-Ромберга:')
    runge_romberg_eiler: list[float] = runge_romberg_richardson_method(h, h / 2, y_eiler_h, y_eiler_h_div_2, 1)
    runge_romberg_runge_kutt: list[float] = runge_romberg_richardson_method(h, h / 2, y_runge_kutt_h, y_runge_kutt_h_div_2, 4)
    runge_romberg_adams: list[float] = runge_romberg_richardson_method(h, h / 2, y_adams_h, y_adams_h_div_2, 4)
    print('Набор х: ', *x_exact)
    print('Метод Эйлера: ', *runge_romberg_eiler, end='\n\n')
    print('Метод Рунге-Кутты: ', *runge_romberg_runge_kutt, end='\n\n')
    print('Метод Адамса: ', *runge_romberg_adams, end='\n\n')
    print('Точное решение: ', *y_exact, end='\n\n')

    print('Отклонение от точного решения:')
    print('Метод Эйлера: ', mean_absolute_error(y_eiler_h, y_exact), end='\n\n')
    print('Метод Рунге-Кутты: ', mean_absolute_error(y_runge_kutt_h, y_exact), end='\n\n')
    print('Метод Адамса: ', mean_absolute_error(y_adams_h, y_exact), end='\n\n')

    plt.xlim([1.98, 3.02])
    plt.legend()
    plt.show()