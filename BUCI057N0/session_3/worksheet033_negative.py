# 3. Collect the positive items from a list into a new list and do the same for the negative
#     numbers; ignore zero.
from worksheet030_utils import create_random_list


def split_positive_negative(random_list):
    positive_list = []
    negative_list = []
    for n in random_list:
        if n > 0:
            positive_list.append(n)
        elif n < 0:
            negative_list.append(n)
        else:
            pass
    return positive_list, negative_list


def test_stuff():

    assert split_positive_negative([-1, 0, 1]) == ([1], [-1])


def main():

    random_list = create_random_list(10)
    print('Random list is: {}'.format(random_list))
    p, n = split_positive_negative(random_list)

    print('Positive list is: {}'.format(p))
    print('Negative list is: {}'.format(n))


if __name__ == "__main__":

    test_stuff()
    main()
