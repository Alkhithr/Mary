# Write a function that reads the file words.txt and builds a list with one element per word.
# Write two versions of this function, one using the append method and the other using the idiom t = t + [x].
# Which one takes longer to run? Why?
import time


def build_word_list_a():

    fin = open('words.txt')
    word_list = []

    start = time.time()
    for line in fin:
        word = line.strip()
        word_list.append(word)
    end = time.time()

    print(end-start)


def build_word_list_b():

    fin = open('words.txt')
    word_list = []

    start = time.time()
    for line in fin:
        word = line.strip()
        word_list = word_list + [word]
    end = time.time()

    print(end-start)


def main():

    x = ''

    while x != 'exit':
        x = input('Function A/B?')

        if str.lower(x) == 'a':
            print('Executing build_word_list_a')
            build_word_list_a()
        elif str.lower(x) == 'b':
            print('Executing build_word_list_b')
            build_word_list_b()
        else:
            print('no idea what I\'m doing')


main()
