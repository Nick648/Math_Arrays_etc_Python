import Prov_Numbers


def func(n, v):
    k_o = 0
    s = [0] * 4
    s_o = [0] * 4
    k = [0] * 4
    f = [0] * 4
    for g in range(n):
        for i in range(4):
            f[i] = Prov_Numbers.random.randint(1, (10 ** (i + 1)))
            s_o[i] += f[i]
        # print(f)
        k_o += 1
        for i in range(4):
            if f[i] <= v * (10 ** i):
                k[i] += 1
                s[i] += f[i]
    print("Количество чисел  N =", n, ":")
    print("10: ver = n/m =", k[0] / k_o, ";  sum(n)/sum(m) =", s[0] / s_o[0])
    print("100: ver = n/m =", k[1] / k_o, ";  sum(n)/sum(m) =", s[1] / s_o[1])
    print("1000: ver = n/m =", k[2] / k_o, ";  sum(n)/sum(m) =", s[2] / s_o[2])
    print("10 000: ver = n/m =", k[3] / k_o, ";  sum(n)/sum(m) =", s[3] / s_o[3])


if __name__ == "__main__":
    n, v = 10, 0
    while (v <= 0 or v > 100):
        print("Вероятность должна быть от 1 до 100!")
        v = Prov_Numbers.input_pos_int("Введите вероятность в процентах(%): ")
    v /= 10
    print()
    while n <= 100000:
        func(n, v)
        print("-" * 60)
        n *= 10
