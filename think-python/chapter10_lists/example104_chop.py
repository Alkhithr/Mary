# Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None. For example:


def chop(a_list):
    start = 0
    end = len(a_list)-1

    a_list.pop(end)
    a_list.pop(start)

    return None


def main():

    a_list = [1, 2, 3, 4, 5, 6, 'test', 'test more']
    chop(a_list)
    print(a_list)


main()