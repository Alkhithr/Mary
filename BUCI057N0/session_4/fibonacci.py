import random


def calc_fib(n):
    fib_seq = [0, 1, 1]
    i = 3
    while i <= n:
        next_n = fib_seq[i-2] + fib_seq[i-1]
        fib_seq.append(next_n)
        i += 1
    return fib_seq[n]


def test_me():

    assert calc_fib(10) == 55
    assert calc_fib(20) == 6765


def main():

    n = random.randint(0, 100)
    print(n, ': ', calc_fib(n))


if __name__ == '__main__':
    test_me()
    main()
