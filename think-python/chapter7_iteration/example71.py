import random
import math


def mysqrt(a, x):

    if x <= 0:
        x = random.randrange(0, 100)

    while True:
        print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y


def mysqrt_test(a, x):
    # a   mysqrt(a)     math.sqrt(a)  diff

        a2 = (x + a/x) / 2
        ma2 = math.sqrt(a)
        print(a, a2, ma2, a2 - ma2)


def main():
    # mysqrt(9, 1)
    for a in range(1, 10):
        mysqrt_test(float(a), 1)


main()
