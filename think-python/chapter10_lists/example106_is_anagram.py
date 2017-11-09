# Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they are anagrams.


def is_anagram(w1, w2):

    if len(w1) != len(w2):
        return False

    w1_list, w2_list = [], []

    for w in w1:
        w1_list.append(w)

    for w in w2:
        w2_list.append(w)

    w1_list.sort()
    w2_list.sort()

    for i in range(len(w1_list)):

        if w1_list[i] != w2_list[i]:
            return False

    return True


def main():

    w1, w2 = '', ''

    while w1 != 'exit':

        w1 = input('Word 1: ')
        w2 = input('Word 2: ')

        result = is_anagram(w1, w2)

        print(result)


main()