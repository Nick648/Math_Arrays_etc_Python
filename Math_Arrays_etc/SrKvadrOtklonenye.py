from math import *
import time
import os


def exi_t():  # Выход из программы
    a = 'Спасибо за использование нашего продукта!\nХорошего дня!'
    for i in a:
        print(i, end='')
        time.sleep(0.03)  # Приостановить выполнение программы
    input()
    exit()


def algorithm():  # Основной алгоритм
    a = []
    summa = 0
    dst = 0  # Среднеквадратическое отклонение
    disp = 0  # Дисперсия
    print("Введите данные для нахождения стандартного разброса.")
    print("Для ввода вещественных цифр исользуйте точку.")
    print("Для конца ввода данных введите: '000'.")
    while True:

        s = input()
        if (s.isdigit()):
            if (s == "000"):
                break
            else:
                a.append(int(s))
                summa += int(s)
        else:
            if (s.rfind(".") == s.find(".") and s.find(".") != -1):
                a.append(float(s))
                summa += float(s)
            else:
                os.system('cls')
                print("Нужно вводить только по одной цифре за раз без лишних символов!")
                print("Введите данные для нахождения стандартного разброса.")
                print("Для ввода вещественных цифр исользуйте точку.")
                print("Для конца ввода данных введите: '000'.")
    print("Ваши значения:", a)
    while True:
        print("Если данные верны, то введите '+', если нет, то введите '-'")
        s = input()
        if (s == "+"):
            break
        elif (s == "-"):
            os.system('cls')
            print("Попробуйте ещё раз.")
            return 0
        else:
            print("Введите только '+' или '-'. Других вводов программа не понимает(")
    srznach = summa / len(a)
    for i in range(len(a)):
        disp += (a[i] - srznach) ** 2
    while True:
        print("Выберите вариант выборки(введите '1' или '2'):")
        print("1) Генеральная совокупность(все значения)\n2) Выборка(часть значений)")
        s = input()
        if (s == "1"):
            disp /= len(a)
            break
        elif (s == "2"):
            disp /= (len(a) - 1)
            break
        else:
            os.system('cls')
            print("Введите только '1' или '2'. Других вводов программа не понимает(")
    dst = sqrt(disp)
    v = (dst / srznach) * 100
    os.system('cls')
    print("Ваши значения:", a)
    print("Сумма элементов ряда, summa =", summa)
    print("Среднее значение, srznach =", srznach)
    print("Дисперсия, disp =", disp)
    print("Среднееквадратическое отклонение, dst =", dst)
    print("Коэффициент вариации v = " + str(v) + "%")
    print("\033[35m{}\033[0m".format(
        "- При <10% выборка слабо вариабельна;\n- При 10% – 20 % — средне вариабельна;\n- При >20 % — выборка сильно вариабельна."))
    while True:
        print(
            "Хотите ли какие значения являются среднестатистическими? Если да, то введите '+', если нет, то введите '-'")
        s = input()
        if (s == "+"):
            for i in range(len(a)):
                if (a[i] > (srznach + dst)):
                    print(str(i + 1) + ")", a[i], ": Экстраординарно больше")
                elif (a[i] < (srznach - dst)):
                    print(str(i + 1) + ")", a[i], ": Экстраординарно меньше")
                else:
                    print(str(i + 1) + ")", a[i], ": Среднестатистическое")
            break
        elif (s == "-"):
            break
        else:
            print("Введите только '+' или '-'. Других вводов программа не понимает(")
    print()
    return 1


def main():  # Запуск программы
    os.system('cls')
    print("№ Нахождение среднеквадратического отклонения/Стандартного разброса")
    f = algorithm()
    if (f == 0):
        algorithm()
    exi_t()


main()

import numpy as np

data = np.array([])
while True:
    s = input("Input digits(for stop '000'): ")
    if s == "000":
        break
    else:
        data = np.append(data, int(s))
print(data)
sr = np.mean(data)
srqv = np.std(data)
f = data[abs(data - sr) < srqv]
print(np.sum(data), sr, srqv, f)
