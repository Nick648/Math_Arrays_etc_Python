from math import *
import time, random
import matplotlib.pyplot as plt


# matplotlib
class Equation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_value(self, x):
        return self.__a * x ** 2 + self.__b * x + self.__c

    def output_equ(self):
        x_value, y_value = [], []
        for i in range(-10, 11, 1):
            x_value.append(i)
            y_value.append(self.get_value(i))
        plt.title("y = F(x)")  # заголовок
        plt.xlabel("x")  # ось абсцисс
        plt.ylabel("y")  # ось ординат
        plt.grid()  # включение отображение сетки
        plt.plot(x_value, y_value)  # построение графика
        plt.show()


def exi_t():  # Выход из программы
    seconds = [0.03, 0.04, 0.05, 0.06]
    s = "\nСпасибо за использование нашей программы.\nВсего хорошего!"
    for i in s:
        print(i, end="")
        time.sleep(random.choice(seconds))
    time.sleep(2)
    input()
    exit()


def quad_equation(a, b, c):  # Решение уравнения
    dis = (b ** 2) - (4 * a * c)
    if a > 0:
        print('Парабола с ветвями вверх')
    else:
        print('Парабола с ветвями вниз')
    xv = -b / (2 * a)
    yv = a * (xv ** 2) + b * xv + c
    print('С вершиной в точке: (', xv, '; ', yv, ')', sep='')
    print('Дискриминант:', dis)
    if dis == 0:
        answer = -b / 2 * a
        print('Ответ: x = ', answer, sep='')
    elif dis < 0:
        print('Парабола не пересекает ось ОХ')
        print('Ответ: Решений нет')
    else:
        dis_sqrt = sqrt(dis)
        print('Дискриминант под корнем:', dis_sqrt)
        x1 = (-b + dis_sqrt) / (2 * a)
        x2 = (-b - dis_sqrt) / (2 * a)
        print('Ответ: x1 = ', x1, ';', sep='', end=' ')
        print('x2 = ', x2, sep='')


def linear_equation(b, c):
    if b == 0:
        if c == 0:
            print('0 = 0')
            print('Ответ: x = (-∞; +∞)')

        else:
            print(c, ' = 0', sep='')
            print('Прямая не пересекает ось ОХ')
            print('Ответ: Решений нет')

    else:
        if c == 0:
            print(b, 'x = 0', sep='')
            print('Ответ: x = 0')

        else:
            print(b, 'x =', -c, sep='')
            answer = -c / b
            print('Ответ: x =', answer, sep='')


def qu(s='Введите значение: '):  # Ввод начальных значений
    while True:
        try:
            input_value = int(input(s))
            break
        except ValueError:
            print('НАДО ВВОДИТЬ ТОЛЬКО ЧИСЛА!')
            print('P.S. И строка не должна быть пустой.\n')
    return input_value


def main():  # Основной алгоритм
    print('ax^2+bx+c=s')
    print('Если a,b,c или s отсутствует, то введите 0.\n')
    a = qu('Введите a: ')
    b = qu('Введите b: ')
    c = qu('Введите c: ')
    s = qu('Введите s: ')
    if s != 0:
        c = c - s
    equ = Equation(a, b, c)
    print('Result:\n')
    if a == 0:
        linear_equation(b, c)
    elif a > 0 or a < 0:
        if b == 0:
            if c == 0:
                print(a, 'x^2 = 0', sep='')
                quad_equation(a, b, c)
            else:
                print(a, 'x^2 = ', -c, sep='')
                quad_equation(a, b, c)
        elif b > 0:
            if c == 0:
                print(a, 'x^2 + ', b, 'x = 0', sep='')
                answer = -b / a
                print('Ответ: x = 0; x = ', answer, sep='')
                input()
                exit()
            elif c > 0:
                print(a, 'x^2 + ', b, 'x + ', c, ' = 0', sep='')
                quad_equation(a, b, c)
            elif c < 0:
                print(a, 'x^2 + ', b, 'x -', -c, ' = 0', sep='')
                quad_equation(a, b, c)
        elif b < 0:
            if c == 0:
                print(a, 'x^2 - ', -b, 'x = 0', sep='')
                quad_equation(a, b, c)
            elif c > 0:
                print(a, 'x^2 - ', -b, 'x + ', c, ' = 0', sep='')
                quad_equation(a, b, c)
            elif c < 0:
                print(a, 'x^2 - ', -b, 'x - ', -c, ' = 0', sep='')
                quad_equation(a, b, c)
    equ.output_equ()
    exi_t()


if __name__ == '__main__':
    main()
