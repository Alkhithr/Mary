# Write a function called nested_sum that takes a list of lists of integers and
# adds up the elements from all of the nested lists. For example:


def nested_sum(integer_lists):

    s = 0
    for integer_list in integer_lists:
        s += sum(integer_list)

    return s


def main():

    nested_lists=[[1, 2], [3, 4], [5, 6]]
    print(nested_sum(nested_lists))


main()
