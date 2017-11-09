# Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once.
# It should not modify the original list.


def has_duplicates(n_list):
    result = False
    for n in n_list:
        if n_list.count(n) > 1:
            result = True
            break
    return result


def main():

    n_list = [1, 2, 3]
    assert has_duplicates(n_list) is False

    n_list.append(3)
    assert has_duplicates(n_list) is True


main()
