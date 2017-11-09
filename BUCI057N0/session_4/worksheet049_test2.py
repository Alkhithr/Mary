# 9. Write the following functions and provide a program to test them.
# (a) def allTheSame(x, y, z) (returning true if the arguments are all the same)
# (b) def allDifferent(x, y, z) (returning true if the arguments are all different)
# (c) def sorted(x, y, z) (returning true if the arguments are sorted, with the
# smallest one coming first)
import random


def all_the_same(x, y, z):
    if x == y == z:
        return True
    return False


def all_different(x, y, z):
    if x != y and x != z and y != z:
        return True
    return False


def sorted1(x, y, z):
    if x <= y <= z:
        return True
    return False


def sorted2(x, y, z):

    list_in = []
    list_sort = []
    for n in (x, y, z):
        list_in.append(n)
        list_sort.append(n)

    list_sort.sort()

    if list_in == list_sort:
        return True

    return False


def test_me():
    assert all_the_same(1, 1, 1) is True
    assert all_the_same(1, 1, 0) is False
    assert all_the_same(1, 0, 1) is False
    assert all_the_same(0, 0, 1) is False

    assert all_different(1, 1, 1) is False
    assert all_different(1, 1, 0) is False
    assert all_different(1, 0, 1) is False
    assert all_different(0, 0, 1) is False
    assert all_different(-1, 0, 1) is True

    assert sorted1(1, 2, 3) is True
    assert sorted1(1, 1, 3) is True
    assert sorted1(1, 3, 2) is False
    assert sorted2(1, 2, 3) is True
    assert sorted2(1, 1, 3) is True
    assert sorted2(1, 3, 2) is False


def main():

    high = 1
    low = -1

    x = random.randint(low, high)
    y = random.randint(low, high)
    z = random.randint(low, high)

    print('The numbers {} {} {} are all the same: {}'.format(x, y, z, all_the_same(x, y, z)))
    print('The numbers {} {} {} are all different: {}'.format(x, y, z, all_different(x, y, z)))
    print('The numbers {} {} {} are sorted: {}'.format(x, y, z, sorted1(x, y, z)))


if __name__ == '__main__':
    test_me()
    main()

