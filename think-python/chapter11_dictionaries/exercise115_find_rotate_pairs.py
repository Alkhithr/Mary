# Two words are “rotate pairs” if you can rotate one of them and get the other (see rotate_word in Example 8-5).
# Write a program that reads a wordlist and finds all the rotate pairs.


def find_rotate_pairs(word_list):

    pairs = []
    cool_pairs = []
    for word_l in word_list:
        for word_r in word_list:
            if word_l != word_r:
                search_pair_l = [word_l, word_r]
                search_pair_r = [word_r, word_l]
                if pairs.count(search_pair_l) == 0:
                    pairs.append(search_pair_l)
                if pairs.count(search_pair_r) == 1:
                    pairs.remove(search_pair_r)

    for index in range(0, len(pairs)):
        a = pairs[index][0]
        b = pairs[index][1]
        ord_diff = ord(b[0:1]) - ord(a[0:1])
        rotated_a = ''

        for letter in a:
            rotated_a += chr(ord(letter) + ord_diff)

        if rotated_a == b:
            cool_pairs.append([a, b])

        print('{} rotated by {} is {}. Compare it with it\'s pair {}'.format(a, ord_diff, rotated_a, b))

    return cool_pairs


print(find_rotate_pairs(['selina', 'ibm', 'hal', 'ant', 'bou', 'cpv']))
