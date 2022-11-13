import Prov_Numbers


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


def choice(m, n):
    return fact(n) / (fact(m) * fact(n - m))


if __name__ == "__main__":
    print("C^m n: Выборка")
    a = Prov_Numbers.input_pos_int("Введите сколько выбираем: ")
    b = Prov_Numbers.input_pos_int("Введите из скольки выбираем: ")
    if a > b:
        print("Кол-во всех элементов должно быть больше!\n")
    else:
        print("Количество вариантов:", choice(a, b))
    s = input()
