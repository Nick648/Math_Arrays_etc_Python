def input_distance(s='Enter value: '):  # input kilometres
    while True:
        try:
            input_value = float(input(s))
            break
        except ValueError:
            print('It is necessary to enter only numbers separated by a dot!')
            print("Example: 4.48")
            print('P.S. And the line should not be empty.\n')
    return input_value


def input_time(s='Enter value: '):  # input minutes
    while True:
        arr = input(s).split(':')
        input_value = list()
        if len(arr) == 2 and arr[0].isdigit() and arr[1].isdigit():
            for i in range(2):
                input_value.append(int(arr[i]))
            break
        else:
            print('It is necessary to enter only numbers separated by a colon!')
            print("Example: 12:36")
            print('P.S. And the line should not be empty.\n')
    return input_value


def main():  # The main algorithm
    km = input_distance("Enter kilometers: ")
    times = input_time("Enter minutes: ")
    seconds = times[0] * 60 + times[1]
    pace = seconds / km
    minutes = pace // 60
    seconds = pace % 60
    pace = '%d:%d' % (minutes, seconds)
    print("Pace:", pace)


if __name__ == '__main__':  # Start
    main()
# Add tkinter!
