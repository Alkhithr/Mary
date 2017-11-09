# Write a function called is_abecedarian that returns True if
# the letters in a word appear in alphabetical order (double letters are ok). How many abecedarian words are there?


def letter_alpha_ordinal(letter):

    alphabet = 'abcdefghijklmnopqrstuvxyz'
    return str.find(alphabet, letter)


def is_abecedarian(word):

    i = 0

    while i < len(word):

        if i > 0:

            if letter_alpha_ordinal(word[i-1]) < letter_alpha_ordinal(word[i]):
                return True
            else:
                return False

        i += 1


def main():

    x = ''

    while x != 'exit':

        x = input("word: ")
        print(is_abecedarian(x))


main()

