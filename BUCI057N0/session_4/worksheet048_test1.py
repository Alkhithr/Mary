# 8. Write the following functions and provide a program to test them.
# Page 2
# (a) def smallest(x, y, z) (returning the smallest of the arguments)
# (b) def average(x, y, z) (returning the average of the arguments)
import random


def smallest(x, y, z):
    s = x
    for i in (x, y, z):
        if i < s:
            s = i
    return s


def average(x, y, z):
    total = 0
    count = 0
    for i in (x, y, z):
        total += i
        count += 1

    return total / count


def test_me():

    assert smallest(-1, 0, 1) == -1
    assert average(1, 2, 3) == 2


def main():

    high = 1000
    low = -1000

    x = random.randint(low, high)
    y = random.randint(low, high)
    z = random.randint(low, high)

    print('The lowest number of {}, {}, {} is: {}'.format(x, y, z, smallest(x, y, z)))
    print('The average number of {}, {}, {} is: {}'.format(x, y, z, average(x, y, z)))


if __name__ == '__main__':
    test_me()
    main()
