# Write a function named uses_all that takes a word and a string of required letters, and that
# returns True if the word uses all the required letters at least once.
# How many words are there that use all the vowels aeiou? How about aeiouy?


def uses_all(word, letters):

    l_count = 0

    for l_letter in letters:

        if str.count(word, l_letter) > 1:
            l_count += 1

    if l_count < len(letters):
        return False
    else:
        return True


def main():

    word, letters = '', ''

    while word != 'exit':
        word = input('Word: ')
        letters = input('Letters: ')

        if uses_all(word, letters):
            print('word {} uses all letters from {} more than once'.format(word, letters))
        else:
            print('word {} does not use all letters from {} more than once'.format(word, letters))


main()
