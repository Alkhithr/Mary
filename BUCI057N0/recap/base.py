import random
import time


def random_dec():
    return random.randint(16, 255)


def convert_number(n, base):
    result = None

    if base == 2:
        result = bin(n)
    elif base == 8:
        result = oct(n)
    elif base == 10:
        result = int(n)
    elif base == 16:
        result = hex(n)
    else:
        pass

    return result


def main():
    assert random_dec() < 255
    sep = '-' * 32

    print(sep)
    n = random_dec()
    base_list = [2, 8, 10, 16]
    random_base = base_list[random.randint(0, 3)]
    print('Convert\nbase-{}: \t{}'.format(random_base, convert_number(n, random_base)))
    print(sep)
    time.sleep(10)

    print('Answers')
    print(sep)
    for base in base_list:

        print('base-{}: \t{}'.format(base, convert_number(n, base)))

    print()


main()
