
x = '\tselina is so gorgeous.\tshe is the definition of gorgeous.\t'
print(x)


def log(name, result):
    print(name + ': ' + str(result))


for cmd in ('str.capitalize(x)', 'str.center(x, 80, \'-\')', 'str.count(x, \'gorgeous\')', 'str.encode(x, \'utf-16\', \'strict\')',
            'str.endswith(x, \'.\')', 'str.expandtabs(x, 16)', 'str.find(x,\'lala\')', 'str.format(\'yo yo yo {0}\', x)',
            'str.index(x, \'so\')',  # same as find but raises ValueError if not found
            'str.isalnum(x)', 'str.isdigit(\'123\')', 'str.islower(x)', 'str.isspace(\'     \')', 'str.istitle(x)'
            ):
    out = eval(cmd)
    log(cmd, out)


print('Do more later')
