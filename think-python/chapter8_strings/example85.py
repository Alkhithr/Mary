def rotate_word(word, rotate_by):

    i = 0
    while i < len(word):
        ordinal = ord(word[i])

        print(word[i], ordinal, chr(ordinal + rotate_by), ordinal + rotate_by)

        i += 1


def main():

    x = ''

    while x != 'done':
        x = input('Enter word: ')
        y = input('Enter Integer:')

        rotate_word(x, int(y))


main()
