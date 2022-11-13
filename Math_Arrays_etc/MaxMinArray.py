import random

n = int(input("Кол-во строк и столбцов: "))
a = [[0 for j in range(n)] for i in range(n)]
nmax = 9
nmin = 100
print("\nArray A: ")
for i in range(n):
    for j in range(n):
        k = random.randint(10, 99)
        a[i][j] = k
        if (k >= nmax):
            nmax = k
            imax = i + 1
            jmax = j + 1
        if (k <= nmin):
            nmin = k
            imin = i + 1
            jmin = j + 1
        print('{:4d}'.format(a[i][j]), end=' ')
    print()

print('Максимум=', nmax, '[', imax, ']', '[', jmax, ']')
print('Минимум=', nmin, '[', imin, ']', '[', jmin, ']')

print("\nArray B: ")
for i in range(n):
    for j in range(n):
        k = random.randint(10, 99)
        a[i][j] = k
        print('{:4d}'.format(a[i][j]), end=' ')
    print()

nmax = 9
nmin = 100
for i in range(n):
    kmax = max(a[i])
    kmin = min(a[i])
    if (kmax >= nmax):
        nmax = kmax
    if (kmin <= nmin):
        nmin = kmin

print('Максимум=', nmax, )  # '[', imax, ']', '[', jmax, ']')
print('Минимум=', nmin, )  # '[', imin, ']', '[', jmin, ']')
