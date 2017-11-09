# Write a function named avoids that takes a word and a string of forbidden letters, and
# that returns True if the word doesn’t use any of the forbidden letters.
#
# Modify your program to prompt the user to enter a string of forbidden letters and then
# print the number of words that don’t contain any of them.
# Can you find a combination of 5 forbidden letters that excludes the smallest number of words?


from collections import OrderedDict


def avoids(word, forbidden):
    for w_letter in word:
        for f_letter in forbidden:
            if w_letter == f_letter:
                return False

    return True


def main():

    # forbidden = input('Enter forbidden characters: ')

    forbidden_letters = 'abcdefghijklmnopqrstuvxyz'
    result = {}

    for letter in forbidden_letters:

        fin = open('words.txt')
        counter = 0

        for line in fin:

            word = line.strip()

            if avoids(word, letter):
                counter += 1

        result[letter] = counter

    print(OrderedDict(sorted(result.items(), key=lambda t: t[1])))


main()

# OrderedDict([('e', 37641), ('s', 49006), ('i', 53495), ('a', 57196), ('r', 58908), ('n', 64127), ('t', 66530), ('o', 69152), ('l', 73676), ('d', 83161), ('c', 83343), ('u', 84934), ('g', 88830), ('p', 90840), ('m', 91335), ('h', 94713), ('b', 97504), ('y', 100668), ('f', 102532), ('k', 104831), ('v', 104917), ('z', 110358), ('x', 111118), ('j', 112062), ('q', 112177)])