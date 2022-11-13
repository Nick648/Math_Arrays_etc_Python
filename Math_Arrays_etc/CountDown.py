import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='')
        time.sleep(1)
        print("", end="\r")
        t -= 1

    print("Time's up!")


t = input("Enter the times(in sec): ")
countdown(int(t))
