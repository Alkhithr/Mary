def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def palindrome(word):
    first_word = first(word)
    middle_word = middle(word)
    last_word = last(word)

    result = first_word + ', ' + middle_word + ', ' + last_word

    return result


def main():
    word = input('Type a word here:   ')
    x = palindrome(word)
    print(x)


main()
