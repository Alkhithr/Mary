# Write a function called in_bisect that takes a sorted list and a target value and returns the
# index of the value in the list if it’s there, or None if it’s not.

import bisect


def in_bisect(sorted_word_list, target_value):

    index = bisect.bisect(sorted_word_list, target_value) - 1

    if sorted_word_list[index] == target_value:
        return index

    return None


def main():

    fin = open('words.txt')
    sorted_word_list = []

    for line in fin:
        word = line.strip()
        sorted_word_list.append(word)

    sorted_word_list.sort()

    target_value = ''

    while target_value != 'exit':

        target_value = input('Enter word: ')

        print('Position in list: ', in_bisect(sorted_word_list, target_value))


main()
