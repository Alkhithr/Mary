def calc_factorial(n):

    f = ''
    while n > 1:
        f = f + '{} * {}'.format(n, (n-1))
        n -= 1

    return f


def test_stuff():
    assert calc_factorial(2) == 2


def factorial(n):
    product = 1
    for i in range(n):
        product *= (i+1)
    return product


def fib(n):

    fib_list = [0, 1, 1]
    i = 3
    while i <= n:
        fib_list.append(fib_list[i-2] + fib_list[i-1])
        i += 1

    return fib_list[n]


def fib2(n):
    a = 1
    b = 1
    for i in range(2, n):
        res = a + b
        a = b
        b = res
    return b


def main():

    # f = calc_factorial(5)
    x = fib(10)
    print(x)
    # print(x[len(x)-1])

    print(fib2(10))


main()
