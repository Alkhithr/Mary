import random


def factorial(n):
    fact = 0
    first_n = n
    while n != 1:
        if n != first_n:
            fact = fact * (n - 1)
            # print(fact)
        else:
            fact = first_n * (n - 1)
        n -= 1
    return fact


def test_me():
    assert factorial(5) == (5 * 4 * 3 * 2 * 1)
    assert factorial(10) == 3628800


def main():
    n = random.randint(1, 20)
    print('{}! = {}'.format(n, factorial(n)))


if __name__ == '__main__':
    test_me()
    main()
