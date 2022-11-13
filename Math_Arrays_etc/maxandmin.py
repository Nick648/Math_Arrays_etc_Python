import random

while True:
    try:
        n = int(input('Введите кол-во строк и столбцов: '))
        break
    except ValueError:
        print('НАДО ВВЕСТИ ТОЛЬКО ЧИСЛО!')
        print('P.S. И строка не должна быть пустой.')
        print()
a = [[0 for j in range(n)] for i in range(n)]
max = 9
min = 100
print()
print('A: ')
for i in range(n):
    print('    Строка', end=' ')
    print(i + 1, ')', sep='', end=' ')
    for j in range(n):
        k = random.randint(10, 99)
        a[i][j] = k
        if n == 1:
            max, min = k, k
            im, jm, inn, jn = 0, 0, 0, 0
        else:
            if k >= max:
                max = k
                im = i
                jm = j
            elif k <= min:
                min = k
                inn = i
                jn = j
        print('{:4d}'.format(a[i][j]), end=' ')
    print()
print()
print('Максимум =', max, '[', im + 1, '][', jm + 1, ']')
print('Минимум =', min, '[', inn + 1, '][', jn + 1, ']')
