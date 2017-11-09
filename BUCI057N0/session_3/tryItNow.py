import random


def positive_numbers(int_list):

    total = 0

    for n in int_list:
        if n > 0:
            total += n

    return total


def positive_average(int_list):

    new_int_list = []

    for n in int_list:
        if n > 0:
            new_int_list.append(n)

    if len(new_int_list) > 0:
        return sum(new_int_list) / len(new_int_list)

    return 0


def create_random_list(element_count):

    random_list = []

    odd = True
    while element_count > 0:

        random_int = random.randint(-1000, 1000)
        if odd:
            random_int = -1 * random_int

        odd = not odd

        random_list.append(random_int)

        element_count -= 1

    return random_list


def main():

    test_int_list = [-3, -2, -1, 1, 2, 3]

    assert positive_numbers(test_int_list) == 6
    assert positive_numbers([]) == 0
    assert positive_numbers([-1]) == 0
    assert positive_average(test_int_list) == 2
    assert positive_average([]) == 0
    assert positive_average([-1]) == 0

    list_length = 6
    int_list = create_random_list(list_length)

    x = positive_numbers(int_list)

    print('List {} has a positive sum of {}'.format(int_list, x))

    y = positive_average(int_list)

    print('List {} has a positive average of {}'.format(int_list, y))


main()
