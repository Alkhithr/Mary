fin = open('words.txt')

anagrams = dict()


for line in fin:
    word = line.strip()
    key = []

    for letter in word:
        key.append(letter)

    key.sort()
    key_tuple = tuple(key)

    if anagrams.get(key_tuple) is None:
        anagrams[key_tuple] = [word]
    else:
        anagrams[key_tuple] = anagrams[key_tuple] + [word]
        print(anagrams[key_tuple])


