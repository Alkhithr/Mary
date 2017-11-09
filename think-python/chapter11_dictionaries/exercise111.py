def word_exists(search_word):
    file_in = open('words.txt')
    words = dict()

    result = False

    for line in file_in:
        word = line.strip()
        words[word] = word

    if search_word in words:
        result = True

    return result
