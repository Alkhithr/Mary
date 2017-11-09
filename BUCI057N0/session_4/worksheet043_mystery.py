# 3. Consider this function:
# def mystery(x, y) :
#     result = (x + y) / (y - x)
# return result
# What is the result of the call mystery(2, 3)?


def mystery(x, y):
    result = (x + y) / (y - x)
    return result


def test_me():
    assert mystery(2, 3) == 5


def main():
    x = mystery(2, 3)
    print(x)


if __name__ == '__main__':
    test_me()
    main()
