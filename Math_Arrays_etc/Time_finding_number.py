import random
import time
from colorama import Fore, Style, init

init(autoreset=True)  # Not need RESET at the end massage
# Const module colorama
GREEN = Fore.LIGHTGREEN_EX
RED = Fore.LIGHTRED_EX
YELLOW = Fore.LIGHTYELLOW_EX
CYAN = Fore.LIGHTCYAN_EX
MAGENTA = Fore.LIGHTMAGENTA_EX
RESET = Style.RESET_ALL


def error_out(s):  # Вывод красного текста
    print(RED + s, sep='')


def done_out(s):  # Вывод зелёного текста
    print(GREEN + s, sep='')


def yellow_out(s):  # Вывод жёлтого текста
    print(YELLOW + s, sep='')


def magenta_out(s):  # Вывод фиолетового текста
    print(MAGENTA + s, sep='')


def enter_data(mas):  # Ввод данных
    while True:
        data = input(mas).strip()
        try:
            data = int(data)
            return data
        except ValueError:
            error_out("You must enter a positive INTEGER!\n")


def random_finding(in_number, num_max):
    count_search = 1
    k = random.randint(0, num_max)
    while k != in_number:
        count_search += 1
        k = random.randint(0, num_max)
    return count_search


def min_finding(in_number, num_min, num_max):
    count_search = 1
    k = random.randint(num_min, num_max)
    while k != in_number:
        count_search += 1
        k = random.randint(num_min, num_max)
        if k > in_number:
            num_max = k
        elif k < in_number:
            num_min = k
    return count_search


def smart_finding(in_number, num_min, num_max):
    count_search = 1
    k = num_min + (num_max - num_min) // 2
    while k != in_number:
        count_search += 1
        k = num_min + (num_max - num_min) // 2
        if k > in_number:
            num_max = k
        elif k < in_number:
            num_min = k
    return count_search


def main():
    print(YELLOW + "=" * 30)
    while True:
        total_random_count, total_random_time = 0, 0
        total_min_count, total_min_time = 0, 0
        total_smart_count, total_smart_time = 0, 0
        max_num = enter_data(CYAN + 'Max number: ' + RESET)
        if max_num < 1:
            break
        search_num = enter_data(CYAN + f'Number(1, {max_num}): ' + RESET)
        if search_num < 1 or search_num > max_num:
            break

        for _ in range(1000):
            start_time = time.time()
            count_random_finding = random_finding(search_num, max_num)
            time_random_finding = time.time() - start_time
            total_random_count += count_random_finding
            total_random_time += time_random_finding
        magenta_out(f'\n\tTotal count random finding = {total_random_count};'
                    f'\n\tTotal time = {total_random_time} s;'
                    f'\n\tAverage count random finding = {total_random_count / 1000};'
                    f'\n\tAverage time = {total_random_time / 1000} s;')

        for _ in range(1000):
            start_time = time.time()
            count_min_finding = min_finding(search_num, 0, max_num)
            time_min_finding = time.time() - start_time
            total_min_count += count_min_finding
            total_min_time += time_min_finding
        magenta_out(f'\n\tTotal count min finding = {total_min_count};'
                    f'\n\tTotal time = {total_min_time} s;'
                    f'\n\tAverage count min finding = {total_min_count / 1000};'
                    f'\n\tAverage time = {total_min_time / 1000} s;')

        for _ in range(1000):
            start_time = time.time()
            count_smart_finding = smart_finding(search_num, 0, max_num)
            time_smart_finding = time.time() - start_time
            total_smart_count += count_smart_finding
            total_smart_time += time_smart_finding
        magenta_out(f'\n\tTotal count smart finding = {total_smart_count};'
                    f'\n\tTotal time = {total_smart_time} s;'
                    f'\n\tAverage count smart finding = {total_smart_count / 1000};'
                    f'\n\tAverage time = {total_smart_time / 1000} s;')

        total_count = total_random_count + total_min_count + total_smart_count
        total_time = total_random_time + total_min_time + total_smart_time
        done_out(f'\nTotal count = {total_count};'
                 f'\nTotal time = {total_time} s;'
                 f'\nAverage count/time = {total_count/total_time} try/sec;')
        print(YELLOW + "=" * 30)


if __name__ == '__main__':
    main()
    error_out('\tBye!')
