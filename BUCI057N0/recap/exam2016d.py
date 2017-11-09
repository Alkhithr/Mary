# (d) Write a function called nested_sum that takes a list of lists of integers and
# adds up the elements from all of the nested lists. For example:
# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> nested_sum(t)
# 21


def nested_sum(t):
    total = 0
    for index in range(0, len(t)):
        if type(t[index]) == list:
            total += nested_sum(t[index])
        else:
            total += t[index]
    return total


lst = [1, [2, 3], 4, [5, 6], [7, [8, 9]]]
assert nested_sum(lst) == 45
