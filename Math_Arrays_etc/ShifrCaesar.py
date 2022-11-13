import time

global RUS
global ENG
RUS = []
ENG = []

for i in range(1040, 1072):
    RUS.append(i)
    # print(chr(i), end = " ")

for i in range(65, 91):
    ENG.append(i)
    # print(chr(i), end = " ")

global N1
global N2
N1 = len(RUS)
N2 = len(ENG)


def exi_t():  # Выход из программы
    a = "Спасибо за использование нашего продукта!\nХорошего дня!\n"
    for i in a:
        print(i, end='')
        time.sleep(0.03)  # Приостановить выполнение программы
    input()
    exit()


def shifr():  # Шифрование
    s = input("Строка: ")
    h = int(input("Шаг: "))
    s = s.upper()
    s1 = ""
    for i in range(len(s)):
        if (ord(s[i]) > 1039 and ord(s[i]) < 1072):
            h = h % N1
            k = (ord(s[i]) + h) % 1072
            if (k < 1040):
                k += 1040
        elif (ord(s[i]) > 64 and ord(s[i]) < 91):
            h = h % N2
            k = (ord(s[i]) + h) % 91
            if (k < 65):
                k += 65
        else:
            k = ord(s[i])
        s1 += chr(k)

    print("Полученная строка: ")
    print(s1.lower(), "\n")


def deshifr():  # Расшифровка
    s = input("Строка: ")
    h = int(input("Шаг: "))
    s = s.upper()
    s1 = ""
    for i in range(len(s)):
        if (ord(s[i]) > 1039 and ord(s[i]) < 1072):
            h = h % N1
            k = ord(s[i]) - h
            if (k < 1040):
                k += N1
        elif (ord(s[i]) > 64 and ord(s[i]) < 91):
            h = h % N2
            k = ord(s[i]) - h
            if (k < 65):
                k += N2
        else:
            k = ord(s[i])
        s1 += chr(k)

    print("Полученная строка: ")
    print(s1.lower(), "\n")


def qu():  # Выбор варианта событий
    a = ["1", "2", "3"]
    while True:
        t = input('Вариант: ')
        print()
        if t not in a:
            print('Такого варианта нет! Пожалуйста выберите из предложенного.\n')
        else:
            return int(t)


def main():  # Старт программы
    print("Шифр Цезаря")
    print("Выберите вариант работы программы: ")
    while True:
        print("1) Шифрование\n2) Расшифровка\n3) Выход")
        t = qu()
        if t == 1:
            shifr()
        elif t == 2:
            deshifr()
        elif t == 3:
            exi_t()
    exi_t()


main()
# mmgmkmсусеусселфс56пю()юmvo:;;"''vnv"fqmg32defabcгдеабв
