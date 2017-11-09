import math


def check_fermat(a, b, c, n):

    formula = (str(a) + '**' + str(n) + '+' + str(b) + '**' + str(n) + '=' + str(c) + '**' + str(n))
    print(formula)
    formula = str(int(math.pow(a, n))) + '+' + str(int(math.pow(b, n))) + '=' + str(int(math.pow(c, n)))
    print(formula)

    if n > 2 and math.pow(a, n) + math.pow(b, n) == math.pow(c, n):
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn’t work.')


def main():

    a = input('a:')
    b = input('b:')
    c = input('c:')
    n = input('n:')

    check_fermat(int(a), int(b), int(c), int(n))


main()
