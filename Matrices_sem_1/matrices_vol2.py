def out(a,n):
    for i in range(n):
        for j in range(n):
            print("\033[33m{:4d}\033[0m".format(a[i][j]),end=' ')
        print()
    print()
    return
  
def qu(naz,k,naz_k):
    a=[]
    for i in range(k):
        a.append(str(i+1))
    while True:
	print("\033[7m{}\033[0m".format('/'+naz+')'),' Выберите нужный вариант:')
	for i in range(k):
            print(str(i+1)+')',naz_k[i])
	print()
	t=input("\033[33m{}\033[0m".format('Вариант:'))
	print()
	if t not in a:
            print("\033[1m\033[31m{}\033[0m".format('Такого варианта нет! Пожалуйста выберите из предложенного.\nМы работаем над разнообразием функций.\n'))
	else:
	    return int(t)

def kol_n():
    while True:
        n = input("\033[35m{}\033[0m".format('Введите кол-во строк и столбцов:'))
        if n.isdigit() and int(n)>0:
            return int(n)
	elif not(n.isdigit()):
            print("\033[1m\033[31m{}\033[0m".format('\nНадо ввести положительную цифру!\nЕсли хотите вернуться введите 0.\n'))
	elif n=='0':
            print()
	    main()

def kol_nm():
    while True:
        n = input("\033[35m{}\033[0m".format('Введите кол-во строк n:'))
	if n.isdigit() and int(n)>0:
            n = int(n)
	    break
	elif not(n.isdigit()):
            print("\033[1m\033[31m{}\033[0m".format('\nНадо ввести положительную цифры!\nЕсли хотите вернуться введите 0.\n'))
	elif n=='0':
	    print()
	    main()
    while True:
        m = input("\033[35m{}\033[0m".format('Введите кол-во столбцов m:'))
	if m.isdigit() and int(m)>0:
            return n,int(m)
        elif not(m.isdigit()):
            print("\033[1m\033[31m{}\033[0m".format('\nНадо ввести положительную цифры!\nЕсли хотите вернуться введите 0.\n'))
        elif m=='0':
            print()
            main()
	
def mat_2(a):
    S=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return S
	
def mat_per(a,j,n):
    c=[[]*n]*n
    for i in range(1,n+1):
        b=[]
	for g in range(n+1):
            if g!=j:
                b.append(a[i][g])
                c[i-1]=b
    return mat_n(c,n)

def mat_n(a,n):
    if n>2:
        S=0
	for j in range(n):
            S+=a[0][j]*((-1)**(1+j+1))*mat_per(a,j,n-1)
            return S
    else:
        return mat_2(a)

def opr():
    n=kol_n()
    print("\033[33m{}\033[0m".format('Элементы матрицы вводите строками через пробелы.\n'))
    a=[[0]*n]*n
    for i in range(n):
        print("\033[35m{}\033[0m".format(str(i+1)+' Строка:'))
	l=list(map(int,input().split()))
	for j in range(n):
            a[i]=l
    S=mat_n(a,n)
    print()
    print("\033[33m{}\033[0m".format('Первоначальная матрица:'))
    out(a,n)
    print("\033[32m{}\033[0m".format('Определитель S = '+str(S)),'\n')

def dif():
    naz='Меню/Другое'
    k=6
    naz_k=['Найти x(n)','Умножение','Сложение','Вычитание','Вернуться','Выход']
    t=qu(naz,k,naz_k)
    if t==6:
        print("\033[32m{}".format('Спасибо за использование нашего продукта!\n'))
	input()
	exit()
    elif t in [1,3,4]:
	print("\033[34m{}\033[0m".format('В разработке! :(\n'))
	main()
    elif t==2:
	multi()
    elif t==5:
	main()

def multi():
    naz='Меню/Другое/Умножение'
    k=3
    naz_k=['На число','На матрицу','Вернуться']
    t=qu(naz,k,naz_k)
    if t==3:
        dif()
    elif t==1:
	n,m=kol_nm()
	print(n,m)
			

def main():
    naz='Меню'
    k=3
    naz_k=['Определитель','Другое','Выход']
    t=qu(naz,k,naz_k)
    if t==3:
        print("\033[32m{}".format('Спасибо за использование нашего продукта!\n'))
	input()
	exit()
    elif t==1:
	opr()
	main()
    elif t==2:
        dif()
main()
