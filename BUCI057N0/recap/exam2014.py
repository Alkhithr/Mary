def compute_sum(L):
    total = 0
    for i in range(0, len(L)):
        if i % 2 == 0:
            total += L[i]
        else:
            total -= L[i]
    return total


def get_fib(n):
    fib = [0, 1, 1]
    i = 3
    while len(fib) <= n:
        fib.append(fib[i-1] + fib[i-2])
        i += 1
    return fib[n], fib


def not_string(x):
    result = 'not ' + x
    if x[0:3] == 'not':
        result = x
    return result


def missing_char(x, n):
    return x[0:n] + x[n:]


def main():
    # L = [3, 4, 5, 10]
    # print('the sum of {} is:'.format(L, compute_sum(L)))
    # print('The {} position of the fib sequence is {}'.format(21, get_fib(21)))

    # n = 0
    # n_list = []
    #
    # while n != 99:
    #     n = int(input('Enter number: '))
    #     n_list.append(n)
    #
    # n_list = n_list[:-1]
    # total = 1
    # for i in range(0, len(n_list)):
    #     if i % 2 == 0:
    #         print(n_list[i])
    #         total *= n_list[i]

    # print('The every other product of {} is {}'.format(n_list, total))

    assert not_string('not') == 'not'
    assert not_string('antonio') == 'not antonio'
    assert not_string('antonio not') == 'antonio not'
    assert not_string('candy') == 'not candy'

    assert missing_char('kitten', 1) == 'ktten'
    assert missing_char('kitten', 0) == 'itten'
    assert missing_char('kitten', 4) == 'kittn'

main()

