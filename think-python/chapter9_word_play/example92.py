# Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.
# Modify your program from the previous section to print only the words that have no “e” and
# compute the percentage of the words in the list that have no “e”.


def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
            break

    return True


def main():

    total = 0
    e_count = 0

    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        total += 1
        if has_no_e(word):
            print(word)
            e_count += 1

    print(e_count / total * 100)


main()