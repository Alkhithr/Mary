# Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise.


def is_sorted(a_list):

    b_list, c_list = [], []

    for a in a_list:
        b_list.append(a)
        # c_list.append(a)

    b_list.sort()
    # c_list.reverse()

    for i in range(len(a_list)):
        # print(a_list[i], b_list[i])
        if a_list[i] != b_list[i]:
            return False

    return True


def main():

    a_list = [3, 1, 2, 5, 4]
    print(a_list)
    x = is_sorted(a_list)

    print(x)

    b_list = [1, 2, 3]
    print('\n', b_list)

    x = is_sorted(b_list)

    print(x)


main()
