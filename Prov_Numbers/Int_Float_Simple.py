import random


def input_pos_int(s="int(>0): "):  # Ввод положительных данных int
    while True:
        t = input_int(s)
        if int(t) > 0:
            return int(t)
        else:
            print("\nЧисло должно быть целое положительное!\n")


def input_pos_float(s="float(>0): "):  # Ввод положительных данных float
    while True:
        t = input_float(s)
        if float(t) > 0:
            return float(t)
        else:
            print("\nЧисло должно быть положительное!\n")


def input_int(s="int: "):  # Ввод данных int
    while True:
        t = input(s)
        if t.isdigit() or (t[0] == '-' and t[1:].isdigit()):
            return int(t)
        else:
            print("\nВы должны ввести целое ЧИСЛО!\n")


def input_float(s="float: "):  # Ввод данных float
    while True:
        t = input(s)
        if t.find('.') == t.rfind('.') and t.find('.') != -1:
            if (t[t.find('.') + 1:].isdigit() and t[:t.find('.')].isdigit() or (
                    t[0] == '-' and t[1:t.find('.')].isdigit() and t[:t.find('.')].isdigit())):
                return float(t)
            else:
                print("\nВвод вещественных чисел через точку!")
                print("Пример: 2.0\n")
        else:
            print("\nВвод вещественных чисел через точку!")
            print("Пример: 2.0\n")


def if_pos_int(k):  # Проверка положительности данных int
    try:
        if if_int(k):
            if int(k) > 0:
                return 1
            else:
                return 0
        else:
            return 0
    except ValueError:
        return 0


def if_pos_float(k):  # Проверка положительности данных float
    try:
        if if_float(k):
            if float(k) > 0:
                return 1
            else:
                return 0
        else:
            return 0
    except ValueError:
        return 0


def if_int(k):  # Проверка данных int
    try:
        _ = int(k)
        return 1
    except ValueError:
        return 0


def if_float(k):  # Проверка данных float
    try:
        _ = float(k)
        return 1
    except ValueError:
        return 0


def if_simple(k):  # Проверка на простое число
    if if_pos_int(k):
        k = int(k)
        for i in range(k - 1, 1, -1):
            if k % i == 0:
                return 0
        return 1
    else:
        return 0


if __name__ == '__main__':
    pass
