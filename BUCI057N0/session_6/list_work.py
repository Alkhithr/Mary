import random


def create_random_list(element_count):
    random_list = [0]
    odd = True
    while element_count > 0:
        random_int = random.randint(-128, 128)
        if odd:
            random_int = -1 * random_int
        odd = not odd
        random_list.append(random_int)
        element_count -= 1
    return random_list


def insert2(lst, position, value):
    lst_a = []
    lst_b = []
    for i in range(0, len(lst)):
        if i < position:
            lst_a.append(lst[i])
        else:
            lst_b.append(lst[i])

    return lst_a + [value] + lst_b


def insert3(lst, position, value):
    lst_a = lst[0:position]
    lst_b = lst[position:]
    return lst_a + [value] + lst_b


def test_me():
    assert insert2([1, 3], 0, 2) == [2, 1, 3]
    assert insert2([1, 3], 1, 2) == [1, 2, 3]
    assert insert2([1, 3], 2, 2) == [1, 3, 2]


def main():
    lst = create_random_list(5)
    position = random.randint(0, len(lst))
    value = None

    print('List: {}\nPosition: {}\nValue: {}\nNew list: {}'.format(lst, position, value, insert2(lst, position, value)))
    print('List: {}\nPosition: {}\nValue: {}\nNew list: {}'.format(lst, position, value, insert3(lst, position, value)))


if __name__ == '__main__':
    test_me()
    main()
