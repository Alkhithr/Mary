# Example 9-1.
# Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace).


def character_count(word):

    no_whitespace = str.replace(word, ' ', '')
    return len(no_whitespace)


def main():

    fin = open('words.txt')

    for line in fin:
        word = line.strip()
        if character_count(word) > 20:
            print(word)


main()
