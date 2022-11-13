import time  # модуль time


def isint(n):  # проверка целости числа
    return int(n) == float(n)


def out_mv(a, n, m):  # вывод вещественных матриц
    for i in range(n):
        for j in range(m):
            print("{:9.5f}".format(a[i][j]), end=' ')
        print()
    return


def out_m(a, n, m):  # вывод матриц
    F = True
    for i in range(n):
        for j in range(m):
            F = isint(a[i][j])
            if not F:
                break
        if not F:
            break
    if not F:
        out_mv(a, n, m)
    else:
        for i in range(n):
            for j in range(m):
                print("{:5d}".format(a[i][j]), end=' ')
            print()
    print()
    return


def exi_t():  # Выход из программы
    a = 'Спасибо за использование нашего продукта!\nХорошего дня!'
    for i in a:
        print(i, end='')
        time.sleep(0.03)  # приостановить выполнение программы
    input()
    exit()


def qu(naz, k, naz_k):  # выбор варианта событий
    a = []
    for i in range(k):
        a.append(str(i + 1))
    while True:
        print('/' + naz + ')', ' Выберите нужный вариант для работы с матрицей:')
        for i in range(k):
            print(str(i + 1) + ')', naz_k[i])
        print()
        t = input('Вариант:')
        print()
        if t not in a:
            print(
                'Такого варианта нет! Пожалуйста выберите из предложенного.\nМы работаем над разнообразием функций.\n')
        else:
            return int(t)


def kol_nm():  # ввод кол-ва строк матриц
    while True:

        n = input('Введите кол-во строк n:')

        if n.isdigit() and int(n) > 0:
            break

        elif not (n.isdigit()):
            print('\nНадо ввести положительную цифру!\nЕсли хотите вернуться введите 000.\n')

        elif n == '000':
            print()
            main()

        elif n == '0':
            print('\nНадо ввести положительную цифру!\nЕсли хотите вернуться введите 000.\n')

    return int(n)


def in_nm(n, ps):  # ввод матриц
    while True:
        a = [[]] * n
        F = False
        k = []
        print('Элементы матрицы вводите строками через пробелы.\n')
        for i in range(n):
            print(str(i + 1) + ' Строка:')
            l = list(input().split())
            if len(l) not in k:
                k.append(len(l))
            if len(k) > 1:
                F = True
                print(
                    'В каждой строке должно быть одинаковое кол-во элементов!\nЕсли элемент отсутствует, то введите 0.\nЕсли хотите вернуться введите 000.\n')
                break
            if ps == 1:
                if len(l) != n:
                    print(
                        '\nМатрица долдна быть квадратной!\nP.S. Кол-во элемнтов столбца равно кол-ву строк.\nЕсли элемент отсутствует, то введите 0.\nЕсли хотите вернуться введите 000.\n')
                    F = True
                    break
            for g in l:
                if not (g.isdigit()):
                    if g[0] != '-':
                        print('\nНадо ввести ЧИСЛА матрицы через пробелы!\nЕсли хотите вернуться введите 000.\n')
                        F = True
                else:
                    if g == '000':
                        F = True
                        main()
            if F:
                break
            a[i] = list(map(int, l))
        if len(a[n - 1]) != 0:
            break
    return a


def mat_2(a):  # определитель матрицы 2х2
    S = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return S


def mat_per(a, j, n):  # преобразование матриц n в n-1. для определителя
    c = [[] * n] * n
    for i in range(1, n + 1):
        b = []
        for g in range(n + 1):
            if g != j:
                b.append(a[i][g])
        c[i - 1] = b
    return mat_n(c, n)


def mat_n(a, n):  # определитель n-ой матрицы
    if n > 2:
        S = 0
        for j in range(n):
            S += a[0][j] * ((-1) ** (1 + j + 1)) * mat_per(a, j, n - 1)
        return S
    else:
        return mat_2(a)


def opr():  # оформление определителя
    n = kol_nm()
    print('Для нахождения определителя матрица должна быть квадратной!\nP.S. Скрлько строк, столько и столбцов.')
    a = in_nm(n, 1)
    S = mat_n(a, n)
    print()
    print('Первоначальная матрица:')
    out_m(a, n, n)
    print('Определитель S = ' + str(S), '\n')
    main()


def multi():  # оформление умножения
    naz = 'Меню/Другое/Умножение'
    k = 3
    naz_k = ['На число', 'На матрицу', 'Вернуться']
    t = qu(naz, k, naz_k)
    if t == 1:
        multi_k()
    elif t == 2:
        multi_mm()
    elif t == 3:
        main()


def multi_k():  # умножение на число оформление
    n = kol_nm()
    a = in_nm(n, 0)
    m = len(a[0])
    print()
    while True:
        k = input('Введите число на которое умножаем:')
        if k.isdigit():
            if k == '000':
                print()
                main()
            else:
                k = int(k)
                break
        elif not (k.isdigit()):
            if k[0] == '-' and k[:1].isdigit:
                k = int(k)
                break
            else:
                print('\nНадо ввести число!\nЕсли хотите вернуться введите 000.\n')
    print('\nПервоначальная матрица:')
    out_m(a, n, m)
    if n == m:
        S = mat_n(a, n)
        print('Определитель S = ' + str(S), '\n')
    c = multi_k1(a, n, k)
    print('Полученная матрица:')
    out_m(c, n, m)
    if n == m:
        print('Определитель S = ' + str(S), '\n')
    main()


def multi_k1(a, n, k):  # умножение на число
    m = len(a[0])
    c = [[]] * n
    for i in range(n):
        b = []
        for j in range(m):
            b.append(a[i][j] * k)
        c[i] = b
    return c


def in_mm2():  # ввод двух матриц
    print('Матрица A:')
    n1 = kol_nm()
    a1 = in_nm(n1, 0)
    m1 = len(a1[0])
    print('\nМатрица B:')
    n2 = kol_nm()
    a2 = in_nm(n2, 0)
    m2 = len(a2[0])
    return n1, a1, m1, n2, a2, m2


def out_mm3(a1, a2, c, n1, n2, n3, m1, m2, m3):  # вывод трёх матриц
    print('\nПервоначальная матрица A:')
    out_m(a1, n1, m1)
    if n1 == m1:
        S1 = mat_n(a1, n1)
        print('Определитель матрицы A;  S1 = ' + str(S1), '\n')
    print('Первоначальная матрица B:')
    out_m(a2, n2, m2)
    if n2 == m2:
        S2 = mat_n(a2, n2)
        print('Определитель матрицы B;  S2 = ' + str(S2), '\n')
    print('Полученная матрица С:')
    out_m(c, n3, m3)
    if n3 == m3:
        S3 = mat_n(c, n1)
        print('Определитель матрицы C;  S3 = ' + str(S3), '\n')


def multi_mm():  # умножение матриц оформление
    while True:
        n1, a1, m1, n2, a2, m2 = in_mm2()
        if m1 == n2:
            break
        else:
            print(
                '\nДля умножения матриц вторая должна иметь столько же строк, сколько столбцов у первой!\nЕсли хотите вернуться введите 000.\n')
    c = multi_mm1(a1, a2, n1, n2, m1, m2)
    out_mm3(a1, a2, c, n1, n2, n1, m1, m2, m2)
    main()


def multi_mm1(a1, a2, n1, n2, m1, m2):  # умножение матриц
    c = [[]] * m2
    for i in range(n1):
        b = []
        for j in range(m2):
            k = 0
            for g in range(n2):
                k += a1[i][g] * a2[g][j]
            b.append(k)
        c[i] = b
    return c


def transp():  # оформление транспонирования
    n = kol_nm()
    a = in_nm(n, 0)
    m = len(a[0])
    c = transp1(a, n, m)
    print('\nПервоначальная матрица:')
    out_m(a, n, m)
    if n == m:
        S1 = mat_n(a, n)
        print('Определитель первоначальной матрицы;  S1 = ' + str(S1), '\n')
    print('Полученная матрица:')
    out_m(c, m, n)
    if m == n:
        S2 = mat_n(c, m)
        print('Определитель полученной матрицы;  S2 = ' + str(S2), '\n')
    main()


def transp1(a, n, m):  # транспонирование
    c = [[a[j][i] for j in range(n)] for i in range(m)]
    return c


def sv_m():  # оформление меню сложения/вычитания
    naz = 'Меню/Сложечитание'
    k = 3
    naz_k = ['Сложение матриц', 'Вычитание матриц', 'Вернуться']
    t = qu(naz, k, naz_k)
    if t == 1:
        sv_m1(1)
    elif t == 2:
        sv_m1(2)
    elif t == 3:
        main()


def sv_m1(k):  # сложение/вычитание матриц оформление
    while True:
        n1, a1, m1, n2, a2, m2 = in_mm2()
        if n1 == n2 and m1 == m2:
            n = n1 = n2
            m = m1 = m2
            break
        else:
            print(
                '\nДля сложения/вычитания матрицы должны быть одинаковые!\nP.S. Иметь одинаковое кол-во строк и столбцов.\nЕсли хотите вернуться введите 000.\n')
    c = sv_m2(a1, a2, n, m, k)
    n3, m3 = n, m
    out_mm3(a1, a2, c, n1, n2, n3, m1, m2, m3)
    main()


def sv_m2(a1, a2, n, m, k):  # сложение/вычитание матриц
    c = [[]] * n
    for i in range(n):
        b = []
        for j in range(m):
            if k == 1:
                b.append(a1[i][j] + a2[i][j])
            elif k == 2:
                b.append(a1[i][j] - a2[i][j])
        c[i] = b
    return c


def x_n():  # нахождение Xn оформление
    while True:
        n1, a1, m1, n2, a2, m2 = in_mm2()
        if (n1 != m1 and n2 != m2) or (m1 != 1 and m2 != 1) or (n1 != n2):
            print(
                '\nДля нахождения Xn матрицы необходимо, чтобы одна была квадратной, а другая имела один столбец и столько же строк, сколько и в первой!\nP.S. Квадратная - это матрица, которая имеет одинаковое кол-во строк и столбцов.\nЕсли хотите вернуться введите 000.\n')
        else:
            break
    n = n1
    if m1 > m2:
        m = m1
    else:
        m = m2
        m1, m2 = m2, m1
        a2, a1 = a1, a2
    k = -1
    b1, b2 = [], []
    for g in range(m):
        k += 1
        c = [[]] * n
        c = x_n1(a1, a2, n, m, k, c)
        b1.append(c)
        b2.append(mat_n(c, n))
    print('\nПервоначальная матрица A:')
    out_m(a1, n1, m1)
    if n1 == m1:
        S = mat_n(a1, n1)
        print('Определитель матрицы;  S = ' + str(S), '\n')
    print('Первоначальная матрица B:')
    out_m(a2, n2, m2)
    if n2 == m2:
        S = mat_n(a2, n2)
        print('Определитель матрицы;  S = ' + str(S), '\n')
    print()
    for g in range(m):
        print('Матрица ' + str(g + 1) + ':')
        a, b = b1[g], b2[g]
        out_m(a, n, m)
        print('Определитель матрицы ' + str(g + 1) + ';  S' + str(g + 1) + ' = ' + str(b), '\n')
    print('Xn = Sn/S\n')
    print('Ответ:', end=' ')
    if S != 0:
        for i in range(len(b2)):
            h = b2[i] / S
            if isint(h):
                print('X' + str(i + 1) + ' = ', str(b2[i] / S) + ';  ')
            else:
                print('X' + str(i + 1) + ' = ',
                      str(b2[i] / S) + ' или X' + str(i + 1) + ' =' + str(b2[i]) + '/' + str(S) + ';  ')
    else:
        print('Решений нет! Так как определитель главной матрицы равен 0, а на ноль делить нельзя.')
    print()
    main()


def x_n1(a1, a2, n, m, k, c):  # нахождение Xn
    for i in range(n):
        b = []
        for j in range(m):
            if j == k:
                b.append(a2[i][0])
                continue
            b.append(a1[i][j])
        c[i] = b
    return c


def minors_m(a, n, m):  # Миноры матрицы
    am = [[]] * n
    for i in range(n):
        b = []
        for j in range(m):
            k = 0
            c = [[]] * (n - 1)
            c = new_m(a, c, n, m, k, i, j)
            s = mat_n(c, (n - 1))
            b.append(s)
        am[i] = b
    return am


def new_m(a, c, n, m, k, i, j):  # Новая матрица для миноров
    for g1 in range(n):
        b = []
        for g2 in range(m):
            if g1 != i and g2 != j:
                b.append(a[g1][g2])
        if g1 != i:
            c[k] = b
            k += 1
    return c


def obrat():  # Обратная матрица оформление
    print(
        'Обратная матрица существует только если:\n- Она квадратная(имеет одинаковое кол-во строк и столбцов)\n- Её определитель не равен нулю\n')
    n = kol_nm()
    a = in_nm(n, 1)
    print('\nПервоначальная матрица:')
    out_m(a, n, n)
    S1 = mat_n(a, n)
    print('Определитель первоначальной матрицы;  S1 = ' + str(S1), '\n')
    if S1 == 0:
        print('Определитель равен нулю! Обратной матрицы не существует.\n')
    else:
        c = minors_m(a, n, n)
        for i in range(n):
            f = []
            for j in range(n):
                f.append(c[i][j] * ((-1) ** (i + 1 + j + 1)))
            c[i] = f
        c = transp1(c, n, n)
        for i in range(n):
            f = []
            for j in range(n):
                f.append(c[i][j] / S1)
            c[i] = f
        print('\nПолученная матрица:')
        out_m(c, n, n)
        S2 = mat_n(c, n)
        print('Определитель полученной матрицы;  S2 = ' + str(S2), '\n')
    main()


def main_mat():  # основное меню
    print()
    naz = 'Меню'
    k = 7
    naz_k = ['Определитель', 'Найти x(n)', 'Умножение', 'Сложение/Вычитание', 'Транспонирование', 'Обратная матрица',
             'Выход']
    t = qu(naz, k, naz_k)
    if t == 1:
        opr()
    elif t == 2:
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


def main():  # Start
    main_mat()  # вызов основного меню


if __name__ == '__main__':
    main()
