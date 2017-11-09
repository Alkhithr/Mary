# If you did Example 10-7, you already have a function named has_duplicates that takes a list as a
# parameter and returns True if there is any object that appears more than once in the list.
# Use a dictionary to write a faster, simpler version of has_duplicates.


def has_duplicates(n_list):
    n_dict = dict()
    result = False
    for n in n_list:
        if n_dict.get(n) is None:
            n_dict[n] = 1
        else:
            result = True
    return result


def main():

    n_list = [1, 1, 2]
    assert has_duplicates(n_list) is True
    n_list = [1, 2, 3]
    assert has_duplicates(n_list) is False
    n_list = []
    assert has_duplicates(n_list) is False


main()
