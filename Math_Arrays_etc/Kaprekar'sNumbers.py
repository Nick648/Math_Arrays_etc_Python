import Prov_Numbers


def print_Kaprekar_nums(start, end):
    for i in range(start, end + 1):
        # Get the digits from the square in a list:
        sqr = i ** 2
        digits = str(sqr)  # Now loop from 1 to length of the number - 1, sum both sides and check
        length = len(digits)
        for x in range(1, length):
            left = int("".join(digits[:x]))
            right = int("".join(digits[x:]))
            if (left + right) == i:
                print("Number: " + str(i) + "  Sqr: " + str(i ** 2) + "  Left: " + str(left) + "  Right: " + str(right))
    print("\nВсе числа диапазона напечатаны!")


a = Prov_Numbers.input_pos_int("Введите начало отрезка: ")
b = Prov_Numbers.input_pos_int("Введите конец отрезка: ")
print()
if (b > a):
    print_Kaprekar_nums(a, b)
else:
    print_Kaprekar_nums(b, a)
