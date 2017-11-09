# Two words “interlock” if taking alternating letters from each forms a new word.
# For example, “shoe” and “cold” interlock to form “schooled”. Solution: http://thinkpython2.com/code/interlock.py.
# Credit: This exercise is inspired by an example at http://puzzlers.org.
#
# Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!
#
# Can you find any words that are three-way interlocked; that is,
# every third letter forms a word, starting from the first, second or third?

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

    return words


def sorted_words_by_letter_list():

    fin = open('words.txt')
    words = []
    for line in fin:
        word = line.strip().join(sorted(word))

    words.sort()

    return words


def main():

    word_list_sorted = sorted_words_by_letter_list()

    for word_out in word_list_sorted:

        for word_in in word_list_sorted:

            if in_bisect(word_list_sorted, sorted(word_out + word_in)):


main()


# a=ant
# b=onym
# c=antonym
#
# a=ant
# b=mnoy
# c=amnnoty
#
# (a+b)=c