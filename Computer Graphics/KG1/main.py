# Шандрюк Пётр Николаевич
# группа М80-308Б-20
# вариант 5 - x ^ (2 / 3) + y ^ (2 / 3) = a ^ (2 / 3)

import numpy as np
import matplotlib.pyplot as plt

# Задаем константы
user_a = int(input("Введите параметр для графика: "))
power = 2 / 3

# Задаем диапазоны Х
x_list1 = list(np.arange(0, user_a, 0.001))
x_list2 = list(np.arange(-user_a, 0, 0.001))

# Задаем диапазоны Y
y_list1 = [(user_a ** power - x ** power) ** 1.5 for x in np.arange(0, user_a, 0.001)]
y_list2 = [(user_a ** power - x ** power) ** 1.5 for x in np.arange(user_a, 0, -0.001)]
y_list3 = [-((user_a ** power - x ** power) ** 1.5) for x in np.arange(0, user_a, 0.001)]
y_list4 = [-((user_a ** power - x ** power) ** 1.5) for x in np.arange(user_a, 0, -0.001)]

# Отрисовываем графики и отображаем их
ax = plt.axes()
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.title('График уравнения x^(2/3) + y^(2/3) = a^(2/3)')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x_list1, y_list1, color='b')
plt.plot(x_list2, y_list2, color='b')
plt.plot(x_list1, y_list3, color='b')
plt.plot(x_list2, y_list4, color='b')
plt.show()
