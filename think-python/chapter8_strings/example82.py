fruit = 'abanana'

i = 0
counter = 0

while i < len(fruit):
    counter += str.count(fruit, 'a', i, i + 1)
    i += 1

print(counter)

# meh
print(str.count(fruit, 'a'))