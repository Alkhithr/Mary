# Write a program that
# reads a file,
# breaks each line into words,
# strips whitespace and punctuation from the words,
# and converts them to lowercase.

import string
import json

fin = open('pg55650.txt')
word_count = dict()

for line in fin:

    for p in string.punctuation:
        line = line.replace(p, '|')

    for w in string.whitespace:
        line = line.replace(w, '|')

    words = line.split('|')

    for word in words:
        if len(word) > 1:
            word = word.lower()
            if word_count.get(word) is None:
                word_count[word] = 1
            else:
                word_count[word] += 1

# get top 20

frequency_ordinal = []
for word in word_count:
    if frequency_ordinal.count(word_count[word]) == 0:
        frequency_ordinal.append(word_count[word])

frequency_ordinal.sort(reverse=True)
word_count_top_20 = dict()

for frequency in frequency_ordinal[0:20]:
    for word in word_count:
        if word_count[word] == frequency:
            if word_count_top_20.get(word) is None:
                word_count_top_20[frequency] = [word]
            else:
                word_count_top_20[frequency] += [word]


print(json.dumps(word_count_top_20, indent=2))






