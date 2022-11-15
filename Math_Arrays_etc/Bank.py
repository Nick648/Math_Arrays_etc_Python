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


def qu(s):  # Ввод данных int
    while True:
        t = input(s)
        print()
        if t.isdigit():
            if int(t) > 0:
                return int(t)
            else:
                print("Число должно быть целое положительное!\n")
        else:
            print("Вы должны ввести целое положительное ЧИСЛО!\n")


def qu_f(s):  # Ввод данных float
    while True:
        t = input(s)
        print()
        if t.find('.') == t.rfind('.') and t.find('.') != -1:
            if float(t) > 0:
                return float(t)
            else:
                print("Число должно быть положительное!\n")
        else:
            print("Вы должны ввести положительное ЧИСЛО!")
            print("Ввод вещественных чисел через точку!\n")


def enter_data(mas, value):  # Ввод данных
    while True:
        data = input(mas).strip()
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


def long_term_contribution():
    s = qu("\nВведите сумму(руб), которую кладём на счёт: ")
    n = qu("Введите на какое количество лет кладём: ")
    p = qu_f("Введите процент банка(в процентах): ")
    s1 = s
    for i in range(1, n + 1):
        s1 += (s1 * (p * 0.01))
        # print("После ", i, "  года: ", S1, " руб.")
    print("После " + str(n) + "-х лет сумма будет: ", s1, "руб.")
    print("Разница между", s, "и", s1, "составляет: ", s1 - s, "руб.")


def short_term_contribution():
    amount = enter_data("\nEnter the full amount (rubles) that we put into the account or deposit: ", 1)
    count = enter_data("Enter for what time we put (in months): ", 1)
    percent = enter_data("Enter the bank's annual percentage (in percent): ", 2)
    month_repl = enter_data("Enter the number of months after which the deposit is replenished: ", 1)

    if month_repl > count:
        done_out(f"After {count} months, the amount on the deposit will be: {amount * 1.0001} rub.")
        yellow_out("Since the number of months of replenishment is more than how much the amount will be, "
                   "the percentage is: 0.01%")
        return

    amount_after = amount
    for i in range(1, count + 1):
        amount_repl = (amount_after * (percent * 0.01)) / 12
        amount_after += amount_repl
        # yellow_out(f"After {i} month: {amount_after} rub.")
    done_out(f"\nAfter {count} months, the amount on the deposit will be: {amount_after} rub.")
    done_out(f"The accumulated amount will be: {amount_after - amount} rub.")


def main():
    text = YELLOW + 'Select an option:\n' \
                    '\t1) Long-term contribution\n' \
                    '\t2) Short-term contribution\n' \
                    '\t3) Exit\n' \
                    'Enter the appropriate number of your choice: ' + RESET
    while True:
        choice = input(text).strip()
        if choice == '1':
            long_term_contribution()  # Долгосрочный вклад (v1)
            break
        elif choice == '2':
            short_term_contribution()  # Краткосрочный вклад (v2)
            break
        elif choice == '3':
            break
        else:
            error_out('Unfortunately, we do not have such an option.\n')


if __name__ == '__main__':
    hello = YELLOW + " The program was created to help with deposits " + RESET
    print("\n", "{:*^75}".format(hello), "\n", sep='')
    main()
    done_out('\nThank you for using our program.\nHave a nice day!')
