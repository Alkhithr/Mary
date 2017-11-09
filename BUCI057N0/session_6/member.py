def member(lst, item):

    if type(item) is list:
        return

    if item in lst:
        return True
    return False


def member2(lst, item):
    result = False
    if type(item) != list:
        for n in lst:
            if n == item:
                result = True
                break
            elif type(n) == list:
                result = member2(n, item)
    return result


def test_me():

    assert member([1, 2, 3], 1)
    assert not member([1, 2, 3], 4)
    assert not member([1, 2, 3], [1])
    #
    assert member2([1, 2, 3], 1)
    assert not member2([1, 2, 3], 4)
    assert not member2([1, 2, 3], [1])
    assert member2([1, [4,5]], 1)
    assert not member2([1, 2, 3, [4, 5]], [1])
    assert not member2([], [])
    assert not member2()


def main():

    print(member([1, 2, 3], 1))
    print(member([1, 2, 3], 0))
    # print(member([1, 2, 3], [1, 2]))


# main()
test_me()
