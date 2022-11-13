import math
import numpy as np


def method(x, t):
    return x * x * math.exp(-1 * t * x);


def func(a, b, n, t, h):
    f = 0;
    print("%-5s" % "i", end=" ")
    for i in range(n):
        print("%10d" % i, end="")
    print()
    print("%-5s" % "x[i]", end=" ")
    for i in range(n):
        print("%7f" % (a + i * h), end="")
    print()
    print("%-5s" % "f(x)", end=" ")
    for i in range(n):
        k = "%4.f" % method(a + i * h, t)
        k.center(10)
        print(k, end="")
        f += method(a + i * h, t);
    print()
    return f * h;


def main():
    print("Функция x^2*e^(-tx)\nПределы интегрирования: a = -1; b = 1;")
    print("Парметр функции: t = 0.5, 1.0, 1.5, 2.0")
    print("Введите кол-во элементарных отрезков, на которые разделяем [a,b]. n: ", end="")
    a, b = -1, 1
    n = int(input())

    while (n <= 0):
        print("Число n не может быть отрицательным или равным нулю!")
        print("Введите кол-во элементарных отрезков, на которые разделяем [a,b]. n: ")
        n = int(input())
    h = (b - a) / n;
    print("Шаг равен h = " + str(h))
    for t in np.arange(0.5, 2.1, 0.5):
        print("\nt = " + str(t) + ": ")
        f = func(a, b, n, t, h);
        print("Интеграл f = " + str(f))


main()
