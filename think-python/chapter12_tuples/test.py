def print_all(*args):
    print(args)


def sum_all(*args):
    total = 0
    for i in args:
        total += i
    return total


assert sum_all(1, 3, 6) == 10


t = (54, 13)
x = divmod(*t)
print(x)
print(t[0] // t[1])
print(t[0] % t[1])
print(sum_all(10,15,11))


a = 'abcd'
b = '1234'
c = '!@£$'

d = zip(a, b, c)
print(type(d))

for x, y, z in d:
    print(x,y,z)

e = list(zip(a, b, c))
print(e)

f = list(d)
print('this isn\'t working', f)


for index, element in enumerate('I love you baby'):
    print(index, element)

numbers = dict()
numbers['antonio', 'one'] = 123
numbers['selina', 'one'] = 345

for last, first in numbers:
    print(first, last, numbers[last, first])
