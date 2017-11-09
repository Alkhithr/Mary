# 1. Sum the values input by the user until they type 99.

def process_input(n, n_list):

    try:
        n_list.append(int(n))
    except ValueError:
        print('ValueError. Input is not a number. Try again.')
    finally:
        return sum(n_list)

    return sum(n_list)


def test_process_input():

    print('Testing process_input ...')

    assert process_input(1, []) == 1
    assert process_input('test-string', []) == 0

    print('Testing successful\n\n')


def main():

    n = 0
    n_list = [n]
    s = sum(n_list)

    while n != '99':

        n = input('Enter a number (99 to terminate):')

        if n != '99':
            s = process_input(n, n_list)
            print('The sum is: {}'.format(s))
        else:
            print('The sum remains: {}. Number 99 has not been added.'.format(s))


if __name__ == "__main__":
    test_process_input()
    main()
