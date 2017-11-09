# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements. For example:


def middle(a_list):
    start = 1
    end = len(a_list)-1
    return a_list[start:end]


def main():

    a_list = [1, 2, 3, 4, 5]
    print(middle(a_list))


main()