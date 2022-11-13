# from Prov_Numbers import Int_Float   use Int_Float.(...)
import Prov_Numbers


def a_p(a=1, b=1):
    print("%-20s" % ("an = (-1)^n*(n^2):"), end="")
    for i in range(a, b + 1):
        s = ((-1) ** i) * (i ** 2)
        print(str(s) + "; ", end="")
    prob()


def b_p(a=1, b=1):
    print("%-20s" % ("an = n^4:"), end="")
    for i in range(a, b + 1):
        s = i ** 4
        print(str(s) + "; ", end="")
    prob()


def c_p(a=1, b=1):
    print("%-20s" % ("an = n+4: "), end="")
    for i in range(a, b + 1):
        s = i + 4
        print(str(s) + "; ", end="")
    prob()


def d_p(a=1, b=1):
    print("%-20s" % ("an = 2^n - 5: "), end="")
    for i in range(a, b + 1):
        s = (2 ** i) - 5
        print(str(s) + "; ", end="")
    prob()


def e_p(a=1, b=1):
    print("%-20s" % ("an = 3^n - 1: "), end="")
    for i in range(a, b + 1):
        s = (3 ** i) - 1
        print(str(s) + "; ", end="")
    prob()


def f_p(a=1, b=1):
    print("%-20s" % ("an = -n-2: "), end="")
    for i in range(a, b + 1):
        s = -i - 2
        print(str(s) + "; ", end="")
    prob()


def prob():
    print("...\n" + "-" * 50 + "|")


def init(a=1, b=1):
    a_p(a, b)
    b_p(a, b)
    c_p(a, b)
    d_p(a, b)
    e_p(a, b)
    f_p(a, b)


print("Sequences:\n")
a = Prov_Numbers.input_pos_int("Введите начало диапазона: ")
b = Prov_Numbers.input_pos_int("Введите конец диапазона: ")
if (b > a):
    init(a, b)
else:
    init(b, a)
