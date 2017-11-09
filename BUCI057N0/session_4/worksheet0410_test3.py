# 10. Write the following functions and provide a program to test them.
# (a) def firstDigit(n) (returning the first digit of the argument)
# (b) def lastDigit(n) (returning the last digit of the argument)!
# (c) def digits(n) (returning the number of digits in the argument)
# For example, firstDigit(1729) is 1, lastDigit(1729) is 9, and digits(1729) is 4
import random


def first_digit(n):
    n_str = str(n)
    return int(n_str[0])


def last_digit(n):
    n_str = str(n)
    return int(n_str[len(n_str)-1])


def digits(n):
    n_str = str(n)
    return len(n_str)


def test_me():
    assert first_digit(123) == 1
    assert last_digit(123) == 3
    assert digits(123) == 3


def main():
    n = random.randint(0, 100000)

    print('The first digit of {} is {}'.format(n, first_digit(n)))
    print('The last digit of {} is {}'.format(n, last_digit(n)))
    print('The total digits of {} are {}'.format(n, digits(n)))


if __name__ == '__main__':
    test_me()
    main()

