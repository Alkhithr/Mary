
fruit = 'banana'
letter = fruit[0]
length = len(fruit)
last_letter = fruit[length-1]

print(letter)
print(last_letter)

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1

for letter in fruit:
    print(letter)

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print(letter + suffix)

fruit = 'mango'
fruit_slice = fruit[1:4]
print(fruit_slice)

# REMEMBER: strings are immutable


def find_first(word, letter):
    i = 0
    while i < len(word):
        if word[i] == letter:
            return i
        i += 1
    return -1


x = find_first('banana', 'n')
print(x)

word = 'yourmum'
upper_word = word.upper()
print(upper_word)


print('m' in 'mango')


print('\n*** is_reverse ***\n')


def is_reverse(word, drow):

    i = 0
    j = len(word) - 1

    if len(word) != len(drow):
        return False

    while i < len(word):

        if word[i] != drow[j]:
            return False

        i += 1
        j -= 1

    return True


x = is_reverse('crap', 'parc')
print(x)
