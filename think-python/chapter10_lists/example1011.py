# Two words are a “reverse pair” if each is the reverse of the other.
# Write a program that finds all the reverse pairs in the word list.

import bisect


def in_bisect(sorted_word_list, target_value):

    index = bisect.bisect(sorted_word_list, target_value) - 1

    if sorted_word_list[index] == target_value:
        return index

    return None


def populate_word_list():

    fin = open('words.txt')

    words = []

    for line in fin:
        word = line.strip()
        words.append(word)

    words.sort()

    return words


def main():

    word_list = populate_word_list()

    for word in word_list:

        drow = word[::-1]

        if in_bisect(word_list, drow):
            print('{} is the reverse of {}'.format(word, drow))


main()
