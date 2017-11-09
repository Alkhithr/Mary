# Write a function named uses_only that takes a word and a string of letters, and that
# returns True if the word contains only letters in the list.
# Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa?”


def uses_only(word, letters):

    l_count = 0

    for l_letter in letters:

        if str.find(word, l_letter) > -1:
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

        if uses_only(word, letters):
            print('word {} uses all letters from {}'.format(word, letters))
        else:
            print('word {} does not use all letters from {}'.format(word, letters))


main()


