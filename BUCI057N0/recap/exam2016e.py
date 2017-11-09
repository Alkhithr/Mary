# (e) Write a function called middle that takes a list and returns a new list that
# contains all but the first and last elements. For example:
# >>> t = [1, 2, 3, 4]
# >>> middle(t)
# [2, 3]


def middle(t):
    return t[1:len(t)-1]


lst = [1, 2, 3]
assert middle(lst) == [2]
lst = [1, 2, 3, 4, -1, 'asd']
assert middle(lst) == [2, 3, 4, -1]
assert type(middle(lst)) == list
