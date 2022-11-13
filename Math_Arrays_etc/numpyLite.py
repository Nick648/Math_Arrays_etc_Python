import keyboard as key
import numpy as np
import random
import time


def kol(s):  # ввод кол-ва строк матриц
    while True:

        n = input(s)

        if n.isdigit() and int(n) > 0:
            break

        elif not (n.isdigit()) or int(n) <= 0:
            print('\nНадо ввести положительную цифру!\nЕсли хотите вернуться введите 000.\n')

        elif n == '000':
            print()
            app()

    return int(n)


def randMat():
    lines = kol('Введите кол-во строк n:')
    columns = kol('Введите кол-во столбцов m:')
    array = np.array(range(lines * columns)).reshape((lines, columns))
    print(array)


def qu(naz, k, naz_k):  # Выбор варианта событий
    a = []
    for i in range(k):
        a.append(str(i + 1))

    print('/' + naz + ')', ' Выберите нужный вариант для работы с матрицей:')
    for i in range(k):
        print(str(i + 1) + ')', naz_k[i])
    print()

    while True:
        t = input('Вариант:')
        print()
        if t not in a:
            print(
                'Такого варианта нет! Пожалуйста выберите из предложенного.\nМы работаем над разнообразием функций.\n')
        else:
            return int(t)


def app():  # Основное меню
    print()
    naz = 'Меню'
    naz_k = ['Рандомная матрица', 'Определитель', 'Найти x(n)', 'Умножение', 'Сложение/Вычитание', 'Транспонирование',
             'Обратная матрица', 'Выход']
    t = qu(naz, len(naz_k), naz_k)
    if t == 1:
        randMat()
    elif t == 2:
        opr()
        x_n()
    elif t == 3:
        multi()
    elif t == 4:
        sv_m()
    elif t == 5:
        transp()
    elif t == 6:
        obrat()
    elif t == 7:
        exi_t()
    elif t == 8:
        exi_t()


if __name__ == '__main__':
    app()  # Вызов основного меню
