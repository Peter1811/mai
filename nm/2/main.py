import sys
import math


EPS = 0.001

class Task1():

    def f(self, x):
        return x * math.exp(x) + x * x - 1

    def df(self, x):
        return (x + 1) * math.exp(x) + 2 * x

    def d2f(self, x):
        return (x + 2) * math.exp(x) + 2

    def phi(self, x):
        res = 1 / (math.exp(x) + x)
        return res

    def dphi(self, x):
        return (-math.exp(x) - 1) / (math.exp(2 * x) + 2 * x * math.exp(x) + x * x)

    def get_q(self, a, b):
        return max(abs(self.dphi(a)), abs(self.dphi(b)))


    def iteration_method(self, eps, a, b):
        print("Метод простых итераций")

        x_prev = (b - a) / 2
        q = self.get_q(a, b)
        cnt_iter = 0

        while True:
            cnt_iter += 1

            x = self.phi(x_prev)

            finish_iter = abs(x - x_prev) * q / (1 - q)
            if finish_iter <= eps:
                break

            x_prev = x

        return x, cnt_iter


    def newton_method(self, eps, a, b):
    
        x_prev = b
        cnt_iter = 0
        while True:
            cnt_iter += 1
            x = x_prev - self.f(x_prev) / self.df(x_prev)
            finish_iter = abs(self.f(x) - self.f(x_prev))
            if finish_iter <= eps:
                break

            x_prev = x

        return x, cnt_iter


    def run(self):
        a, b = map(float, input().split())
        try:
            eps = float(sys.argv[1])
        
        except IndexError:
            eps = 0.001

        x, cnt_iter = self.iteration_method(eps, a, b)

        if abs(self.dphi(x)) < 1:
            print("Условие на производную меньше единицы соблюдается")

        if (abs(self.f(x)* self.d2f(x)) < self.df(x)**2):
            print("Условие сходимости есть!")

        print("Метод простых итераций:")
        print(f"x = {x}")
        print(f"Кол-во итераций: {cnt_iter}")

        if (self.f(a) * self.d2f(a) > 0):
            a, b = b, a
        x, cnt_iter = self.newton_method(eps, a, b)
        
        print("Метод Ньютона:")
        print(f"x = {x}")
        print(f"Кол-во итераций: {cnt_iter}")
        

import numpy as np
import math

def f1(X):
    return 2 * X[0] - math.cos(X[1])


def f2(X):
    return 2 * X[1] - math.exp(X[0])


def df1_dx1(X):
    # df1 / dx1
    return 2


def df1_dx2(X):
    return math.sin(X[1])


def df2_dx1(X):
    return -math.exp(X[0])


def df2_dx2(X):
    return 2


def phi1(X):
    # X1 = phi1(X)
    return math.cos(X[1]) / 2


def phi2(X):
    # X2 = phi2(X)
    return math.exp(X[0]) / 2


def dphi1_dx1(X):
    return 0


def dphi1_dx2(X):
    return -math.sin(X[1]) / 2


def dphi2_dx1(X):
    return math.exp(X[0]) / 2


def dphi2_dx2(X):
    return 0


def L_inf_norm(a):
    """
    Get L_inf norm of array a
    ||a||_inf = max(abs(a))
    """
    abs_a = [abs(i) for i in a]
    return max(abs_a)


def get_q(interval1, interval2):
    """
    Get q coefficient for iteration method
    """
    l1, r1 = interval1
    l2, r2 = interval2
    m1 = (l1 + r1) / 2
    m2 = (l2 + r2) / 2
    x1 = m1 + abs(r1 - l1)
    x2 = m2 + abs(r2 - l2)
    max1 = abs(dphi1_dx1([x1, x2])) + abs(dphi1_dx2([x1, x2]))
    max2 = abs(dphi2_dx1([x1, x2])) + abs(dphi2_dx2([x1, x2]))
    return max(max1, max2)


def iteration_method(phi1, phi2, intervals, eps):
    """
    Find root of system:
    f1(x1, x2) == 0
    f2(x1, x2) == 0
    at interval using iteration method
    x1 = phi1(x1, x2)
    x2 = phi2(x1, x2)
    Returns (x1, x2) and number of iterations
    """
    l1, r1 = intervals[0][0], intervals[0][1]
    l2, r2 = intervals[1][0], intervals[1][1]
    x_prev = [(l1 + r1) * 0.5, (l2 + r2) * 0.5]
    q = get_q(intervals[0], intervals[1])
    iters = 0
    while True:
        iters += 1
        x = [phi1(x_prev), phi2(x_prev)]
        if q / (1 - q) * L_inf_norm([(x[i] - x_prev[i]) for i in range(len(x))]) < eps:
            break
        x_prev = x

    return x, iters


def zeydel(phi1, phi2, intervals, eps):
    """
    Find root of system:
    f1(x1, x2) == 0
    f2(x1, x2) == 0
    at interval using iteration method
    x1 = phi1(x1, x2)
    x2 = phi2(x1, x2)
    Returns (x1, x2) and number of iterations
    """
    l1, r1 = intervals[0][0], intervals[0][1]
    l2, r2 = intervals[1][0], intervals[1][1]
    x_prev = [(l1 + r1) * 0.5, (l2 + r2) * 0.5]
    delta = 0
    #q = get_q(intervals[0], intervals[1])
    iters = 0
    while True:
        iters += 1
        x = [phi1(x_prev), phi2(x_prev)]
        if  L_inf_norm([(x[i] - x_prev[i]) for i in range(len(x))]) < eps:
            break
        x_prev = x

    return x, iters


def newton_method(f1, f2, df1_dx1, df1_dx2, df2_dx1, df2_dx2, intervals, eps):
    """
    Find root of system:
    f1(x1, x2) == 0
    f2(x1, x2) == 0
    at intervals using newton method
    Returns x1, x2 and number of iterations
    """
    l1, r1 = intervals[0][0], intervals[0][1]
    l2, r2 = intervals[1][0], intervals[1][1]
    x_prev = np.array([(l1 + r1) / 2, (l2 + r2) / 2])
    jacobi = []
    jacobi.append([df1_dx1(x_prev), df1_dx2(x_prev)])
    jacobi.append([df2_dx1(x_prev), df2_dx2(x_prev)])

    if (np.linalg.norm(np.array(jacobi)) < 1):
        print("Условие сходимости выполнено!")
        
    if (np.linalg.det(np.array(jacobi)) == 0):
        print("матрица вырождена")
    jacobi_inversed = np.linalg.inv(np.array(jacobi))
    iters = 0
    while True:
        iters += 1
        x = x_prev - jacobi_inversed @ np.array([f1(x_prev), f2(x_prev)])
        if L_inf_norm([(x[i] - x_prev[i]) for i in range(len(x))]) < eps:
            break
        x_prev = x

    return x, iters

if __name__ == '__main__':
    task_1 = Task1()
    task_1.run()