import random


def check_prime(n):
    i = 1
    divided_by = []
    while i <= n:
        n_split = str.split(str(n / i), '.')
        if n_split[1] == '0':
            divided_by.append(n_split[0])
        i += 1
    if len(divided_by) == 2:
        result = True
    else:
        result = False
    return result


def test_me():
    assert check_prime(71) is True
    assert check_prime(10) is False


def main():
    n = random.randint(0, 1000)
    is_prime = check_prime(n)

    if is_prime is True:
        print('{} is prime'.format(n))
    else:
        print('{} is not prime'.format(n))


test_me()
main()




