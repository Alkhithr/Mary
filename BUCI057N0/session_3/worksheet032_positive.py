# 2. Add up the positive numbers from a list. Using that function write another function
# that returns the average of the positive numbers.
from worksheet030_utils import create_random_list


def sum_positive(random_list):
    total = 0
    for n in random_list:
        if n > 0:
            total += n
    return total


def avg_positive(random_list):

    total = 0
    count = 0

    for n in random_list:

        if n > 0:
            total += n
            count += 1

    return total / count


def test_stuff():

    assert sum_positive([10, 1]) == 11
    assert sum_positive([10, -1]) == 10
    assert avg_positive([10, 2]) == 6
    assert avg_positive([10, -1]) == 10


def main():

    random_list = create_random_list(10)
    print('Random list generated: {}'.format(random_list))

    pos_sum = sum_positive(random_list)
    print('Positive sum is: {}'.format(pos_sum))

    pos_avg = avg_positive(random_list)
    print('Positive avg is: {}'.format(pos_avg))


if __name__ == "__main__":
    test_stuff()
    main()
