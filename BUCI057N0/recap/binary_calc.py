import random


def random_dec():
    n = 16
    return [random.randint(0, n), random.randint(n, n * 2)]


def main():

    n = random_dec()

    x = bin(n[1])
    y = bin(n[0])
    z0 = bin(n[1] + n[0])
    z1 = bin(n[1] - n[0])
    z2 = bin(n[1] * n[0])
    z3 = bin(n[1] // n[0])

    print(x)
    print(y)

    try:
        input('Press any button to see the answer')
    except NameError:
        pass

    print('{} + {} = {}'.format(x, y, z0))
    print('{} - {} = {}'.format(x, y, z1))
    print('{} * {} = {}'.format(x, y, z2))
    print('{} // {} = {}'.format(x, y, z3))


main()

