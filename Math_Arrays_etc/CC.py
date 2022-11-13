def num(i):
    a, b = [], []
    for g in range(21):
        a.append(chr(g + 65))
        b.append(g + 10)
        if i == a[g]:
            return b[g]
        elif i == b[g]:
            return a[g]


while True:
    while True:
        n = input("\033[35m{}\033[0m".format('Введите в какой СС число:'))
        if n.isdigit() and int(n) > 0:
            n = int(n)
            break
        elif not (n.isdigit()):
            print("\033[1m\033[31m{}\033[0m".format(
                '\nНадо ввести положительную цифру!\nЕсли хотите выйти введите 000.\n'))
        elif n == '000':
            print()
            exi_t()

    while True:
        m = input("\033[35m{}\033[0m".format('Введите в какую СС переводим число:'))
        if m.isdigit() and int(m) > 0:
            m = int(m)
            break
        elif not (m.isdigit()):
            print("\033[1m\033[31m{}\033[0m".format(
                '\nНадо ввести положительную цифру!\nЕсли хотите выйти введите 000.\n'))
        elif n == '000':
            print()
            exi_t()

    while True:
        a = input("\033[35m{}\033[0m".format('Введите число:'))
        for i in a:
            if not (i.isdigit()):
                i = num(i)
            if i >= n:
                print("\033[1m\033[31m{}\033[0m".format(
                    '\nВ числе не может быть числа больше, чем сама СС числа.\nP.S. Для n-ой СС числа принадлежат промежутку [0;n-1]\n'))
        if a.isdigit() and int(a) > 0:
            a = int(a)
            break
        elif not (m.isdigit()):
            print("\033[1m\033[31m{}\033[0m".format(
                '\nНадо ввести положительную цифру!\nЕсли хотите выйти введите 000.\n'))
        elif n == '000':
            print()
            exi_t()

    a = input('\nВведите число:')
    if n != 10:
        s = 0
        k = len(a) - 1
        for i in a:
            if i.isdigit():
                i = int(i)
            else:
                i = num(i)
            s += i * (n ** k)
            k -= 1
        a = s
        print('\nВ десятичной СС:', a)
    s = ''
    if m != 10:
        a = int(a)
        while a > 0:
            k = a % m
            if k > 9:
                k = num(k)
            s = str(k) + s
            a //= m
        print('\nВ', m, 'СС:', s)
    print()
