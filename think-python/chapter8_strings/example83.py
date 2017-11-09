def is_palindrome(word):
    if word != word[::-1]:
        return False

    return True


def main():

    x = ''

    while x != 'done':
        x = input('Type a word: ')
        y = is_palindrome(x)
        print(y)


main()

