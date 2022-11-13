P = 300  # Общая доступная сумма
S = 338  # Общая доступная площадь
R = 0  # Общая начальная производительность
p1, p2, p3 = 10, 7, 5  # Цена каждой машины
s1, s2, s3 = 9, 8, 3  # Площадь каждой машины
r1, r2, r3 = 8, 6, 3  # Производительность каждой машины
i, j, k = 0, 0, 0  # Изначальные количества каждой машины
I, J, K = 0, 0, 0  # Запомнить кол-во нужное
print("Программа по вычислению покупки кол-ва нужных машин с макс производительностью.\n")
f = open('test.txt', 'w')
F = 0  # Кол-во вариантов
while True:
    j, k = 0, 0
    while True:
        k = 0
        while True:
            P_i = p3 * k + p2 * j + p1 * i
            S_i = s3 * k + s2 * j + s1 * i
            R_i = r3 * k + r2 * j + r1 * i
            if (P_i > P or S_i > S):
                break
            else:
                F += 1
                s = "i:", str(i), "j:", str(j), "k:", str(k), "P_i:", str(P_i), "S_i:", str(S_i), "R_i:", str(R_i)
                s = "%-2s%8s%10s%8s%10s%8s%10s%8s%10s%8s%10s%7s" % (s)
                # s = "i: " + str(i) + "x; j: " + str(j) + "x; k: " + str(k) + "x; P_i: " + str(P_i) + "$; S_i: " + str(S_i) + "m^2; R_i: " + str(R_i)
                # print("i: ", i, "x; j: ", j, "x; k: ", k, "x; P_i: ", P_i, "$; S_i: ", S_i, "m^2; R_i: ", R_i)
                f.write(s + "\n")
                if (R_i > R):
                    R, I, J, K = R_i, i, j, k
                k += 1
        P_i = p2 * j + p1 * i
        S_i = s2 * j + s1 * i
        if (P_i > P or S_i > S):
            break
        else:
            j += 1
    P_i = p1 * i
    S_i = s1 * i
    if (P_i > P or S_i > S):
        break
    else:
        i += 1
s = "Максимальная производительность R = " + str(R) + "\nПри i = " + str(I) + "; j = " + str(J) + "; k = " + str(
    K) + "\n"
f.write(s)
f.write("Количество возможных вариантов F = " + str(F) + "\n")
print("Максимальная производительность R = ", R)
print("Yeeees")
f.close()
