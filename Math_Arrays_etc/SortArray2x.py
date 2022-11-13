import random

a = []
k = random.randint(10, 20)
for i in range(k):
    x = random.randint(10, 99)
    a.append(x)
print('K: ', k)
print()
print('A: ', *a)
for i in range(k - 1):
    for j in range(i + 1, k):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print()
print('Sort A: ', *a)
for i in range(k - 1):
    for j in range(i + 1, k):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
print()
print('Sort A(::-1): ', *a)

# New arr
print("\nNew sort random Array\n")

a = []
k = random.randint(7, 17)
for i in range(k):
    h = random.randint(10, 99)
    a.append(h)
print('K:', k)
print('A:', a)
for i in range(k - 1):
    for o in range(i + 1, k):
        if a[i] < a[o]:
            a[i], a[o] = a[o], a[i]
print('New A:', a)
