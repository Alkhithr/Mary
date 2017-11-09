# This question should be answered using the Python programming language.
# (a) Write a program which repeatedly reads numbers until the user enters
# “done”. Once “done” is entered, print out the total, count, and average
# of the numbers. If the user enters anything other than a number, detect
# their mistake using try and except and print an error message and skip to
# the next number.
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333


def read_and_calc(lst):
    total = 0
    count = 0
    for i in range(0, len(lst)):
        total += lst[i]
        count += 1

    return [total, count, total/count]


def test_me():
    lst = [1, 2, 3]
    assert read_and_calc(lst) == [6, 3, 2]


def main():
    n = 0
    lst = []
    while n != 'done':
        n = input('Enter a number: ')
        try:
            n_int = int(n)
            lst.append(n_int)
        except ValueError:
            if n != 'done':
                print('Invalid input')

    result = read_and_calc(lst)
    print('list: {}\ntotal: {}\ncount: {}\naverage: {}'.format(lst, result[0], result[1], result[2]))


test_me()
main()
