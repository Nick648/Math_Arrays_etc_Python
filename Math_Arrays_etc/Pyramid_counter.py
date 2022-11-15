from colorama import Fore, Style, init

init(autoreset=True)

# Const module colorama
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL


def error_out(s):  # Вывод красного текста
    print(RED + s, sep='')


def done_out(s):  # Вывод зелёного текста
    print(GREEN + s, sep='')


def yellow_out(s):  # Вывод жёлтого текста
    print(YELLOW + s, sep='')


def isint(n):  # проверка целости числа
    try:
        return int(n) == float(n)
    except ValueError:
        print('Not digit!')
        return False


def enter_data(mas, value=1):  # Ввод данных
    while True:
        data = input(mas).strip()
        if value == 1:
            if data == '-':
                return data
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
        else:
            error_out('\nProgrammer error! The programmer is A SUCKER...\n')


def counter_items(floors, card=0):
    count = 0
    for i in range(1, floors + 1):
        if card == 0:
            count += i
        else:
            count += i * 2
            if i > 1:
                count += (i - 1)
    return count


def find_floor(items, card=0):
    floors = 1
    while items > 0:
        floors += 1
        if card == 0:
            items -= floors
        else:
            items -= floors * 2
            if floors > 1:
                items -= (floors - 1)
    return floors - 1


def floor_info(floors, height_floor, card):
    info_floor = f'\n{"*" * 20}\n'
    info_floor += f'\tFloors = {floors}:\n'
    info_floor += f'\tHeight = {floors * height_floor} cm;\n'
    info_floor += f'\tNumber of towers on the lower floor = {floors};\n'
    info_floor += f'\tNumber of elements for the tower = {counter_items(floors, card)};'
    return info_floor


def get_info_height(height, height_floor, card=0):
    floors = int(height // height_floor)
    info = floor_info(floors, height_floor, card)
    floors += 1
    info += floor_info(floors, height_floor, card) + f'\n{"*" * 20}\n'
    return info


def get_info_floors(count_items, height_floor, card=0):
    floors = find_floor(count_items, card)
    info = floor_info(floors, height_floor, card)
    info += f'\n\tThere will be no elements left: {count_items - counter_items(floors, card)};'
    info += f'\n{"*" * 20}\n'
    return info


def pyramid_of_cards():
    height = enter_data('Введите приблизительную желательную высоту пирамиды в сантиметрах: ', 2)
    length_card = enter_data('Введите приблизительную длину карты в сантиметрах: ', 2)
    # Bicycle Standard card length = 8.8 cm
    height_floor = length_card * 0.96592582628907  # length_card * sin(75) -> standard angle = 75 degrees
    if height < height_floor:
        error_out(f'Height ({height}) < Height of floor ({height_floor})!')
        return
    info = get_info_height(height, height_floor, 1)
    done_out(info)
    in_mas = "Введите желательное количество элементов пирамиды.\n" \
             "Если не имеет значения, то введите: '-' \n>>> "
    count_items = enter_data(in_mas, 1)
    if count_items != '-':
        info = get_info_floors(count_items, height_floor, 1)
        done_out(info)


def pyramid_of_glasses():
    height = enter_data('Введите приблизительную желательную высоту пирамиды в сантиметрах: ', 2)
    height_floor = enter_data('Введите приблизительную длину стакана в сантиметрах: ', 2)
    if height < height_floor:
        error_out(f'Height ({height}) < Height of floor ({height_floor})!')
        return
    info = get_info_height(height, height_floor)
    done_out(info)
    in_mas = "Введите желательное количество элементов пирамиды.\n" \
             "Если не имеет значения, то введите: '-' \n>>> "
    count_items = enter_data(in_mas, 1)
    if count_items != '-':
        info = get_info_floors(count_items, height_floor)
        done_out(info)


def qu():  # выбор варианта событий
    a = ['1', '2']
    options = ['Из карт (и подобного)', 'Из стаканчиков (и подобного)']
    while True:
        print('Введите нужный вариант для работы с пирамидой:')
        for i in range(2):
            print(f'{a[i]}) {options[i]};')
        t = input('\nВариант: ')
        if t in a:
            return t
        else:
            error_out('Такого варианта нет! Пожалуйста выберите из предложенного.'
                      '\nМы работаем над разнообразием функций.\n')


def main():
    option = qu()
    if option == '1':
        pyramid_of_cards()
    elif option == '2':
        pyramid_of_glasses()


if __name__ == '__main__':
    greeting = 'Assistance in building a pyramid'
    greeting = YELLOW + greeting + RESET
    print("*" * 10, greeting, "*" * 10, sep=' ', end='\n')
    main()
