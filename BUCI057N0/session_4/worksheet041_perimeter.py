# 1. Write a program that calculates the perimeter and area of a rectangle. The user
# should provide the required values as input.


def calculate(calc_type, side_a, side_b):

    result = 0
    if calc_type.lower() == 'a':
        result = (side_a * side_b)
    elif calc_type.lower() == 'p':
        result = (side_a + side_b) * 2
    else:
        print('You are a bum')

    return result


def test_stuff():

    assert calculate('A', 2, 3) == 6
    assert calculate('P', 2, 3) == 10


def main():

    side_a = int(input('Enter side A: '))
    side_b = int(input('Enter side B: '))
    calc_type = str(input('What would you like to calculate? Area or perimeter? (a/p): '))

    r = calculate(calc_type, side_a, side_b)

    print('Result: {}'.format(r))


if __name__ == '__main__':
    test_stuff()
    main()
