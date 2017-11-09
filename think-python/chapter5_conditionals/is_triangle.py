def is_triangle(len_a, len_b, len_c):

    if len_a + len_b > len_c and len_b + len_c > len_a and len_c + len_a > len_b:
        print('Yep this is good')
    else:
        print('not a triangle')


def main():

    a = input('Stick A length:')
    b = input('Stick A length:')
    c = input('Stick A length:')

    is_triangle(a, b, c)


main()