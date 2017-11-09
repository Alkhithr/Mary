import math


def countdown(n):
    if n <= 0:
        print('Boom!')
    else:
        print(n)
        countdown(n-1)


def recurse(n, s):
    if n == 0:
        print(n, s)
    else:
        recurse(n-1, n+s)
        print(n-1, n+s)


def area(radius):
    a = math.pi * radius ** 2
    return a


def main():
    # countdown(5)
    # recurse(3, 0)
    # recurse(-1, 0)
    x = area(11)
    print (x)


main()

