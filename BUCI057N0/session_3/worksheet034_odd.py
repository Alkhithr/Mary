# 4. For a list of numbers subtract the odd numbers from the running total and add the
# even numbers to the running total.
from worksheet030_utils import create_random_list


def add_subtract(random_list):
    total = 0
    for n in random_list:
        if n % 2 == 0:
            total += n
        elif n % 2 != 0:
            total -= n
    return total


def test_stuff():
    assert add_subtract([1, -1]) == 0


def main():
    random_list = create_random_list(10)
    total = add_subtract(random_list)
    print('My randomly generated list is: {} with -odd+pos total of: {}'.format(random_list, total))


if __name__ == "__main__":
    test_stuff()
    main()
