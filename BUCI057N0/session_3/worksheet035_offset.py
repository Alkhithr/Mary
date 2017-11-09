# 5. Sum the numbers with a specified offset.
from worksheet030_utils import create_random_list
import random


def sum_offset(random_list, offset_list):
    total = 0
    for i in offset_list:
        total += random_list[i]
    return total


def test_stuff():
    assert sum_offset([0, 1, 2, 3, 4, 5], [1, 2]) == 3


def main():
    n = 10
    m = 5
    random_list = create_random_list(n)
    offset_list = []

    for i in range(0, m):
        offset_list.append(random.randint(0, n))

    total = sum_offset(random_list, offset_list)
    print('The randomly generated list is: {}. The total of offsets {} is: {}'.format(random_list, offset_list, total))


if __name__ == '__main__':
    test_stuff()
    main()
