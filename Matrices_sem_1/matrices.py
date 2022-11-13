def mat2(a):
	S=a[0][0]*a[1][1]-a[0][1]*a[1][0]
	return S

def mat3(a):
	S=0
	for j in range(3):
		S+=a[0][j]*((-1)**(1+j+1))*mat32(a,j)
	return S

def mat32(a,j):
	c=[[]*2]*2
	for i in range(1,3):
		b=[]
		for g in range(3):
			if g!=j:
				b.append(a[i][g])
		c[i-1]=b
	return mat2(c)

def mat4(a):
	S=0
	for j in range(4):
		S+=a[0][j]*((-1)**(1+j+1))*mat43(a,j)
	return S

def mat43(a,j):
	c=[[]*3]*3
	for i in range(1,4):
		b=[]
		for g in range(4):
			if g!=j:
				b.append(a[i][g])
		c[i-1]=b
	return mat3(c)

def mat5(a):
	S=0
	for j in range(5):
		S+=a[0][j]*((-1)**(1+j+1))*mat54(a,j)
	return S

def mat54(a,j):
	c=[[]*4]*4
	for i in range(1,5):
		b=[]
		for g in range(5):
			if g!=j:
				b.append(a[i][g])
		c[i-1]=b
	return mat4(c)

def opr():
	n =int(input('Введите кол-во строк и столбцов:'))
	print('Элементы матрицы вводите строками через пробелы')
	print()
	a=[[0]*n]*n
	for i in range(n):
		print(i+1,'Строка:')
		l=list(map(int,input().split()))
		for j in range(n):
			a[i]=l
	if n==2:
		S=mat2(a)
	elif n==3:
		S=mat3(a)
	elif n==1:
		S=a[0][0]
	elif n==4:
		S=mat4(a)
	print()
	print('Полученная матрица:')
	for i in range(n):
		for j in range(n):
			print(a[i][j],end=' ')
		print()
	print()
	print('Определитель S =',S)
	print()

while True:
	print('Выберите нужный вариант:')
	print('1) Определитель')
	print('2) Другое')
	print('3) Выход')
	print()
	t=input('Вариант:')
	print()
	if t!='1' and t!='2' and t!='3':
		print('Такого варианта нет! Пожалуйста выберите из предложенного.')
		print('Мы работаем над разнообразием функций.')
		print()
	elif t=='3':
		print('Спастибо за использование нашего продукта!')
		exit()
	elif t=='1':
		opr()
	elif t=='2':
		print('В разработке! :(')
		print()
	