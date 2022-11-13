import time #модуль time

def out_m(a,n,m): #вывод матриц
    for i in range(n):
        for j in range(m):
            print("{:5d}".format(a[i][j]),end=' ')
        print()
    print()
    return

def exi_t(): #выход из программы
    a = 'Спасибо за использование нашего продукта!\nХорошего дня!'
    for i in a:
        print(i,end='')
        time.sleep(0.04) #приостановить выполнение программы
    input()
    exit()
    
def qu(naz,k,naz_k): #выбор варианта событий
    a=[]
    for i in range(k):
        a.append(str(i+1))
    while True:
        print('/'+naz+')',' Выберите нужный вариант для работы с матрицей:')
        for i in range(k):
            print(str(i+1)+')',naz_k[i])
        print()
        t=input('Вариант:')
        print()
        if t not in a:
            print('Такого варианта нет! Пожалуйста выберите из предложенного.\nМы работаем над разнообразием функций.\n')
        else:
            return int(t)

def kol_nm(k): #ввод кол-ва строк матриц
    while True:
        n = input('Введите кол-во строк n:')
        if n.isdigit() and int(n)>0:
            n = int(n)
            break
        elif not(n.isdigit()):
            print('\nНадо ввести положительную цифру!\nЕсли хотите вернуться введите 000.\n')
        elif n=='000':
            print()
            main()
    if k!=0:
        while True:
            m = input('Введите кол-во столбцов m:')
            if m.isdigit() and int(m)>0:
                m = int(m)
                break
            elif not(m.isdigit()):
                print('\nНадо ввести положительную цифру!\nЕсли хотите вернуться введите 000.\n')
            elif m=='000':
                print()
                main()
        return n,m
    return n

def in_nm(n): #ввод матриц
    while True:
        a = [[]]*n
        F=False
        k=[]
        print('Элементы матрицы вводите строками через пробелы.\n')
        for i in range(n):
            print(str(i+1)+' Строка:')
            l = list(input().split())
            if len(l) not in k:
                k.append(len(l))
            if len(k)>1:
                F=True
                print('В каждой строке должно быть одинаковое кол-во элементов!\nЕсли элемент отсутствует, то введите 0.\nЕсли хотите вернуться введите 000.\n')
                break
            for g in l:
                if not(g.isdigit()):
                    if g[0]!='-':
                        print('\nНадо ввести ЧИСЛА матрицы через пробелы!\nЕсли хотите вернуться введите 000.\n')
                        F=True
                else:
                    if g=='000':
                        F=True
                        main()
            if F:
                break
            a[i] = list(map(int,l))
        if len(a[n-1])!=0:
            break
    return a
    
def mat_2(a): #определитель матрицы 2х2
    S=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return S
	
def mat_per(a,j,n): #преобразование матриц n в n-1. для определителя
    c=[[]*n]*n
    for i in range(1,n+1):
        b=[]
        for g in range(n+1):
            if g!=j:
                b.append(a[i][g])
        c[i-1]=b
    return mat_n(c,n)

def mat_n(a,n): #определитель n-ой матрицы
    if n>2:
        S=0
        for j in range(n):
            S+=a[0][j]*((-1)**(1+j+1))*mat_per(a,j,n-1)
        return S
    else:
        return mat_2(a)

def opr(): #оформление определителя
    n=kol_nm(0)
    print('Для нахождения определителя матрица должна быть квадратной!\nP.S. Скрлько строк, столько и столбцов.')
    a=in_nm(n)
    S=mat_n(a,n)
    print()
    print('Первоначальная матрица:')
    out_m(a,n,n)
    print('Определитель S = '+str(S),'\n')

def dif(): #меню другое
    naz='Меню/Другое'
    k=6
    naz_k=['Найти x(n)','Умножение','Сложение/Вычитание','Транспонирование','Вернуться','Выход']
    t=qu(naz,k,naz_k)
    if t==6:
        exi_t()
    elif t in [1,3]:
        print('В разработке! :(\n')
        main()
    elif t==2:
        multi()
    elif t==5:
        main()
    elif t==4:
        transp()

def multi(): #оформление умножения
    naz='Меню/Другое/Умножение'
    k=3
    naz_k=['На число','На матрицу','Вернуться']
    t=qu(naz,k,naz_k)
    if t==3:
        dif()
    elif t==1:
        multi_k()
    elif t==2:
        multi_mm()

def multi_k(): #умножение на число оформление
    n = kol_nm(0)
    a = in_nm(n)
    m = len(a[0])
    print()
    while True:
        k = input('Введите число на которое умножаем:')
        if k.isdigit():
            if k=='000':
                print()
                main()
            else:
                k = int(k)
                break
        elif not(k.isdigit()):
            if k[0]=='-' and k[:1].isdigit:
                k = int(k)
                break
            else:
                print('\nНадо ввести число!\nЕсли хотите вернуться введите 000.\n')
    print('\nПервоначальная матрица:')
    out_m(a,n,m)
    if n==m:
        S = mat_n(a,n)
        print('Определитель S = '+str(S),'\n')
    c = multi_k1(a,n,k)
    print('Полученная матрица:')
    out_m(c,n,m)
    if n==m:
        print('Определитель S = '+str(S),'\n')
    main()      

def multi_k1(a,n,k): #умножение на число
    m=len(a[0])
    c=[[]]*n
    for i in range(n):
        b=[]
        for j in range(m):
            b.append(a[i][j]*k)
        c[i]=b
    return c			

def multi_mm(): #умножение матриц оформление
    print('Матрица A:')
    n1 = kol_nm(0)
    a1 = in_nm(n1)
    m1 = len(a1[0])
    print('\nМатрица B:')
    n2 = kol_nm(0)
    a2 = in_nm(n2)
    m2 = len(a2[0])
    c=multi_mm1(a1,a2,n1,n2,m1,m2) 
    print('\nПервоначальная матрица A:')
    out_m(a1,n1,m1)
    if n1==m1:
        S1 = mat_n(a1,n1)
        print('Определитель матрицы A;  S1 = '+str(S1),'\n')
    print('Первоначальная матрица B:')
    out_m(a2,n2,m2)
    if n2==m2:
        S2 = mat_n(a2,n2)
        print('Определитель матрицы B;  S2 = '+str(S2),'\n')
    print('Полученная матрица С:')
    out_m(c,n1,m2) 
    if n1==m2:
        S3 = mat_n(c,n1)
        print('Определитель матрицы C;  S3 = '+str(S3),'\n')
    main() 

def multi_mm1(a1,a2,n1,n2,m1,m2): #умножение матриц
    c=[[]]*m2
    for i in range(n1):
        b=[]
        for j in range(m2):
            k=0
            for g in range(n2):
                k+=a1[i][g]*a2[g][j]
            b.append(k)
        c[i]=b
    return c

def transp(): #оформление транспонирования
    n = kol_nm(0)
    a = in_nm(n)
    m = len(a[0])
    c = transp1(a,n,m)
    print('Первоначальная матрица:')
    out_m(a,n,m)
    if n==m:
        S1 = mat_n(a,n)
        print('Определитель первоначальной матрицы;  S1 = '+str(S1),'\n')
    print('Полученная матрица:')
    out_m(c,m,n)
    if m==n:
        S2 = mat_n(c,m)
        print('Определитель полученной матрицы;  S2 = '+str(S2),'\n')
    print()
		
def transp1(a,n,m): #транспонирование
    c = [[]]*m
    for i in range(n):
        for j in range(m):
            b=[]
            for g in range(n):
                b.append(a[g][j])
        c[i]=b
    return c
            
def main(): #основное меню
    naz='Меню'
    k=3
    naz_k=['Определитель','Другое','Выход']
    t=qu(naz,k,naz_k)
    if t==3:
        exi_t()
    elif t==1:
        opr()
        main()
    elif t==2:
        dif()

main() #вызов основного меню
