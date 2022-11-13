import time
from colorama import Fore, Style, init

init(autoreset=True)

# Const module colorama
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL


def error_out(mas):  # Вывод красного текста
    print(RED + mas, sep='')


def done_out(mas):  # Вывод зелёного текста
    print(GREEN + mas, sep='')


def yellow_out(mas):  # Вывод жёлтого текста
    print(YELLOW + mas, sep='')


def enter_data(mas, value):  # Ввод данных
    while True:
        data = input(mas)
        if value == 1:
            try:
                data = int(data)
                if data > 0:
                    return data
                error_out("The number must be a positive integer!\n")
            except ValueError:
                error_out("You must enter a positive INTEGER!\n")
        elif value == 2:
            try:
                data = data.replace(',', '.', 1)
                data = float(data)
                if data > 0:
                    return data
                error_out("The number must be positive!\n")
            except ValueError:
                error_out("You have to enter a positive NUMBER!")


def out(tm_begin, arr):
    print()
    for time_op in arr:
        begin = time.strftime("%H:%M:%S", time.gmtime(tm_begin))
        end = time.strftime("%H:%M:%S", time.gmtime(tm_begin + time_op))
        str_tine = f'Begin: {begin} - End: {end}'
        yellow_out(str_tine)
        tm_begin += time_op


if __name__ == '__main__':
    hello = YELLOW + " The program for see time control day " + RESET
    print("\n", "{:*^75}".format(hello), "\n", sep='')

    h, m, s, = 9, 30, 0  # Set begin time day!
    time_begin = h * 3600 + m * 60 + s
    n = enter_data('Кол-во операций: ', 1)
    ops = []
    for i in range(n):
        t = enter_data('Время в часах: ', 2)
        ops.append(t * 3600)
    out(time_begin, ops)
