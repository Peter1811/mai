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

        if self.f(a) * self.f(b) >= 0:
            print('Значения в точках a и b должны быть разных знаков')
            sys.exit(0)

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
        

if __name__ == '__main__':
    task_1 = Task1()
    task_1.run()
