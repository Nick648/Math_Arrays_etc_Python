import random


def gen(a, b):
    k = random.randint(a, b)
    return k


def cik():
    k = random.randint(-10 ** 5, 10 ** 5)
    print('k = ', k, '\n')
    f = 0
    while True:
        f += 1
        for i in range(2000):
            h = gen(k - 1000, k + 1000)
            if abs(h - n) <= abs(k - n):
                k = h
        print(f, 'поколение:', k, '\n')
        if k == n:
            break
    print("\033[32m{}\033[0m".format('kk ' + str(k)))
    return f


n = int(input('Введите число: '))
s = 0
for i in range(100):
    f = cik()
    s += f
print('Ср.знач =', (s / 100))
