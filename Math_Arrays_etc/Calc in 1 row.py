def pro_calc():
    while True:
        eq = input('>>> ')
        try:
            print(eval(eq))
        except SyntaxError:
            print('SyntaxError: invalid syntax')
        except NameError:
            print(f"NameError: name '{eq}' is not defined")


if __name__ == '__main__':
    # while True: print(eval(input('>>> ')))
    pro_calc()
