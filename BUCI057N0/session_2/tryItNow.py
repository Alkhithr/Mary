def sum_list(a_list):

    if len(a_list) > 0:
        return sum(a_list)
    else:
        return 0


def sum_odd_position_list(a_list):

    total = 0
    for i in range(0, len(a_list)):

        if i % 2 == 0:
            total += a_list[i]

    return total


def sum_odd_position_list_version2(a_list):

    total = 0
    odd = True
    for x in a_list:
        if odd:
            total += x
        odd = not odd

    return total


def ternary_operator()
    if x == 1.3e-50

def main():

    x = [1, 6, 3, 14]
    y = sum_list(x)
    print(y)

    x = []
    y = sum_list(x)
    print(y)

    x = [1, 2, 3, 4, 5, 6]
    #           2     4     6
    y = sum_odd_position_list(x)
    print(y)

    x = [1, 2, 3, 4, 5, 6]
    #           2     4     6
    y = sum_odd_position_list_version2(x)
    print(y)


main()
