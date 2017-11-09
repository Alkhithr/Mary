# 2. Write a function that returns the largest of three numbers provided as arguments
# to the function.
import random


def largest_of_three(n, m, o):

    largest = n

    for i in (n, m, o):
        if i > largest:
            largest = i

    return largest


def test_me():

    assert largest_of_three(1, 2, 3 ) == 3


def main():

    n = random.randint(-1000, 1000)
    m = random.randint(-1000, 1000)
    o = random.randint(-1000, 1000)

    largest = largest_of_three(n, m, o)

    print('The largest of n = {}, m = {}, o = {} is: {}'.format(n, m, o, largest))


if __name__ == '__main__':
    test_me()
    main()
