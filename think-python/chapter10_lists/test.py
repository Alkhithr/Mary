def list_tests():

    cheeses = ['gouda', 'emental', 'jalsberg', 'blue']
    numbers = [1, 123, 456464]
    empty = []

    print(cheeses, numbers, empty)

    cheeses[0] = 'mumcheese'

    print(cheeses)

    print(2 in numbers)

    print(123 in numbers)

    for n in numbers:
        print(n)

    for i in range(len(numbers)):
        print('before:', numbers[i])
        numbers[i] = numbers[i] - 1
        print('after:', numbers[i])

    more_numbers = [456, 76, 97987987]

    numbers = numbers + more_numbers

    print(numbers)

    print(numbers[0:1])
    print(numbers[1:2])
    print(numbers[:])
    print(numbers[2:])
    print(numbers[:3])

    numbers.append(767676)
    print(numbers)

    numbers.extend(more_numbers)

    print(numbers)

    numbers.sort()
    print(numbers)

    cheeses.sort()

    print(cheeses)

    total = sum(numbers)
    print(total)

    print(cheeses.pop())

    cheeses.pop(0)
    print(cheeses)

    del cheeses[0]
    print(cheeses)

    x = 'test1-test2-test3-test4'
    delimiter = '-'
    y = x.split(delimiter)
    print(y)

    delimiter = ','
    z = delimiter.join(y)
    print(z)


def main():
    a = ['a', 'b', 'd', 'c', 'e']
    x = a.count('a')
    a.append('f')
    print(a)
    a.insert(5, 'g')
    a.sort()
    a.reverse()
    a.extend('rst123')
    # a.clear()
    b = a.copy()
    a.pop(0)
    a.append('b')
    a.remove('b')
    a.sort()

    print(a)
    # print(b)




main()
