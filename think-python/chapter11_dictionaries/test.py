en_to_sp = dict()
print(en_to_sp)

en_to_sp['one'] = 'uno'
print(en_to_sp)

en_to_sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(en_to_sp)

print('one' in en_to_sp)
print('four' in en_to_sp)


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d


h = histogram('I love the way you\'re walkin')
print(h)


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('That thing is not here')


def invert_dict(d):
    inverted = dict()
    for key in d:
        val = d[key]
        if val not in inverted:
            inverted[val] = [key]
        else:
            inverted[val].append(key)
    return inverted

# y = reverse_lookup(h, 3)
# print(y)


print(invert_dict(h))

known = {0:0, 1:1}


def fib(n):
    if n in known:
        return known[n]
    res = fib(n-1) + fib(n-2)
    known[n] = res
    return res


print(fib(20))


