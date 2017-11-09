# (f) Write a function called chop that takes a list, modifies it by removing the
# first and last elements, and returns None. For example:
# MSc IT Primer Test 2016 Page 2 of 9
# >>> t = [1, 2, 3, 4]
# >>> chop(t)
# >>> t
# [2, 3]


def chop(t):
    t.pop(0)
    t.pop(len(t)-1)
    return None


lst = [1, 2, 3, 4, 5, 6]
assert chop(lst) is None
assert lst == [2, 3, 4, 5]




