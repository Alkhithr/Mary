def fib(n):
    fib_seq = [1, 1]
    for i in range(2, n):
        index_a = i - 2
        index_b = i - 1
        next_number = fib_seq[index_a] + fib_seq[index_b]
        fib_seq.append(next_number)
        i += 1
    return fib_seq[n-1]


def separate_char(s):
    for i in range(len(s)):
        print(s[i])


def print_digits(s):
    for i in range(len(s)):
        s_char = s[i]
        if s_char.isdigit():
            print(s[i])


def sort_number_list(numbers_in):

    numbers_int = []
    last_char_index = len(numbers_in)

    if numbers_in[last_char_index-1:] == ',':
        numbers_in = numbers_in[0:last_char_index-1]

    numbers_str = numbers_in.split(sep=',')
    for n in numbers_str:
        numbers_int.append(int(n))
    numbers_int.sort()

    return numbers_int


# 1.1. Please write a program whose input is a list A and whose output
# is an index of the smallest element of A. For instance if A=[8,4,3,6,9,9]
# the output should be 2. Notice that `an index' used rather than `the index'.
# This is because of possible multiple occurrences of the smallest element.
# For instance if A=[3,8,3,6,5] then both 0 and 2 are correct outputs.
# For instance you can choose to print the index of the first occurrence
# of the smallest element.

def get_small_from_list(list_input):
    smallest_number_index = 0

    for i in range(len(list_input)):
        if i > 0:
            previous_int = list_input[i-1]
            current_int = list_input[i]

            if previous_int < current_int:
                smallest_number_index = i - 1
            elif current_int < previous_int:
                smallest_number_index = i

    return smallest_number_index


def get_small_from_list2(list_input):
    minimum_index = 0
    minimum_number = list_input[minimum_index]

    for i in range(len(list_input)):
        if list_input[i] < list_input[minimum_index]:
            minimum_index = i
            minimum_number = list_input[i]

    return minimum_index, minimum_number

# 1.2. Please write a program whose input is a list A and whose output
# is the second smallest element of A (the element itself, not its index).
# For instance for  A=[8,4,3,6,9,9], the second smallest element is 4 and
# for A=[3,8,3,6,5], the second smallest element is 3 (the same as the smallest
# one because of the double occurrence).

def get_second_smallest_from_list(list_input):

    first_min_index = 0
    second_min_index = 0

    # get the minimum index
    for i in range(len(list_input)):
        if list_input[i] < list_input[first_min_index]:
            first_min_index = i

    for j in range(len(list_input)):
        if j != first_min_index:
            if list_input[j] < list_input[second_min_index]:
                second_min_index = j

    return '1st {}: {}, 2nd {}: value {}'.format(first_min_index, list_input[first_min_index], second_min_index, list_input[second_min_index])

# 1.3. Let us say that a list A is *sorted* if its elements are stored
# in the ascending order. For instance, A=[1,3,3,4,8,12] is sorted
# while A=[8,10,1,14,16]  is not because 10>1.
# Please write a program whose input is a list A and whose output
# is `sorted' if A is sorted and `not sorted' otherwise.


def is_sorted(list_input, sort_type=1):
    result = ''

    if sort_type == 1:

        for n in range(1, len(list_input)):
            previous_n = n - 1
            current_n = n
            if list_input[previous_n] <= list_input[current_n]:
                result = 'sorted'
            else:
                result = 'not sorted'
                break

    elif sort_type == -1:

        for n in range(1, len(list_input)):
            previous_n = n - 1
            current_n = n
            if list_input[previous_n] > list_input[current_n]:
                result = 'sorted'
            else:
                result = 'not sorted'
                break

    else:

        raise 'boom'

    return result

# 2.1. Please write a program that prints the modules and lists in a report like form
# `module  mark' per line. For instance, for the above lists the corresponding printout will be
# Calculus1 50
# Calculus2 80
# Calculus3 35
# Programming1 70
# Programming2 62
# Programming3 15


def print_modules(modules, marks):
    result = ''
    modules_len = len(modules)
    marks_len = len(marks)
    module_len_max = 0

    if modules_len != marks_len:
        raise 'Inequal row count'

    for i in range(modules_len):
        if len(modules[i]) > module_len_max:
            module_len_max = len(modules[i])

    for i in range(modules_len):
        module_name = modules[i]
        module_len_current = len(module_name)
        if module_len_current < module_len_max:
            post_fix_space = module_len_max - module_len_current
            module_name += post_fix_space * ' '

        result += '{}\t{}\n'.format(module_name, marks[i])

    return result

# 2.2. Please write a program that will produce a report where modules are classifed according
# to the class of the received marks. In particular, the program should first print the lines
# for modules whose mark is first class (>=70) then modules with a 2:1 mark (60-69) then modules
# with a 2:2 mark (50-59), and then failed modules (mark<50). For instance, for the lists as above,
# the printout should something like the following.
#
# Modules with first class marks
# Calculus2 80
# Programming1 70
#
# Modules with 2:1 marks
# Programming2 62
#
# Modules with 2:2 marks
# Calculus1 50
#
# Failed modules
# Calculus3 35
# Programming3 15


def print_modules_classification(modules, marks):
    class_a = 'Modules with first class marks\n'
    class_b = 'Modules with 2:1 marks\n'
    class_c = 'Modules with 2:2 marks\n'
    class_d = 'Failed modules\n'
    modules_len = len(modules)
    marks_len = len(marks)
    module_len_max = 0

    if modules_len != marks_len:
        raise 'Inequal row count'

    for i in range(modules_len):
        if len(modules[i]) > module_len_max:
            module_len_max = len(modules[i])

    for i in range(modules_len):
        module_name = modules[i]
        module_len_current = len(module_name)
        if module_len_current < module_len_max:
            post_fix_space = module_len_max - module_len_current
            module_name += post_fix_space * ' '

        if marks[i] >= 70:
            class_a += '{}\t{}\n'.format(module_name, marks[i])
        elif 60 <= marks[i] < 70:
            class_b += '{}\t{}\n'.format(module_name, marks[i])
        elif 50 <= marks[i] < 60:
            class_c += '{}\t{}\n'.format(module_name, marks[i])
        elif 0 <= marks[i] < 50:
            class_d += '{}\t{}\n'.format(module_name, marks[i])
        else:
            raise ValueError('Illegal mark value')

    return class_a + '\n' + class_b + '\n' + class_c + '\n' + class_d


# 3.1. Please write a program whose input is a string S. The program should treat S as a sequence of numbers
# separated by non-digit symbols. The output of the program are the numbers extracted from S.
# For instance if S="fg123ab34fff45cv576" then the numbers printed should be
# 123
# 34
# 45
# 576


def get_digit_sequences_from_string(string_input):
    # keeping result as string to include leading zeros
    result = ''
    # this is to make string processing easier in the event the last character is numeric
    string_input += '_'

    for i in range(1, len(string_input)):
        previous_char = string_input[i-1]
        current_char = string_input[i]

        if previous_char.isdigit():
            result += str(previous_char)

        if current_char.isdigit() is False and previous_char.isdigit():
            result += '\n'

    return result


# 3.2. Please write a program whose input is a string which is an arithmetical expression with operations `+' and `-'
# and without brackets. The program should evaluate the expression and print the result of the evaluation.
# For instance if S="5+8-7-5+1" then the output should be 2.


def add(a, b):
    print('add:', a, '+', b)
    return a + b


def subtract(a, b):
    print('subtract:', a, '-', b)
    return a - b


def divide(a, b):
    print('divide:', a, '/', b)
    return a / b


def multiply(a, b):
    print('multiply:', a, '*', b)
    return a * b


def calculate(string_input):

    string_input = string_input.replace(' ', '')
    previous_number = ''
    current_number = ''
    new_number = ''
    sign = '_'
    is_first_number = True
    is_first_sign = True

    for s in range(len(string_input)):

        print('\niteration: ', s, end='\n-------------\n')

        if string_input[s].isdigit():
            current_number += string_input[s]
            if is_first_number:
                previous_number = current_number
                print('first number is: ', current_number)
            else:
                print('subsequent number is: ', current_number)
                is_first_sign = False
        elif string_input[s].isdigit() is False and is_first_number:
            sign = string_input[s]
            current_number = ''
            is_first_number = False
            print('sign is: ', sign)

        if is_first_sign is False:
            if sign == '+':
                new_number = add(float(previous_number), float(current_number))
            elif sign == '-':
                new_number = subtract(float(previous_number), float(current_number))
            elif sign == '*':
                new_number = multiply(float(previous_number), float(current_number))
            elif sign == '/':
                new_number = divide(float(previous_number), float(current_number))
            print('intermediate result is:', new_number)

        print('[DEBUG] {} {} {} = {}'.format(previous_number, sign, current_number, new_number), end='\n\n')
    return new_number


if __name__ == '__main__':

    x = '123 * 2 + 3'
    print('\n\nresult ', calculate(x))


if __name__ == '__nothing__':
    fib_index = 20
    print('The fibonacci number at index {} is {}'.format(fib_index, fib(fib_index)))

    x = input("Type something:")
    separate_char(x)
    print('\n')
    print_digits(x)

    x = input("Input a few numbers separated by commas: ")
    print(sort_number_list(x))

    # 1.1
    x = get_small_from_list2([-900, 1, 2, -1, -100, -900, 100, 0, -900, -900])
    print(x)

    # 1.2
    x = get_second_smallest_from_list([-1, -20, -20, -21, 0, 3, 2, 1])
    print(x)

    # 1.3
    x = [0, 1, 2, 3]
    assert is_sorted(x) == 'sorted'
    assert is_sorted(x, 1) == 'sorted'
    assert is_sorted(x, -1) == 'not sorted'
    x = [3, 2, 1, 0]
    assert is_sorted(x) == 'not sorted'
    assert is_sorted(x, 1) == 'not sorted'
    assert is_sorted(x, -1) == 'sorted'
    x = [1, 2, 0, 3]
    assert is_sorted(x) == 'not sorted'
    assert is_sorted(x, 1) == 'not sorted'
    assert is_sorted(x, -1) == 'not sorted'

    # 2.1
    modules = ["Calculus1", "Calculus2", "Calculus3", "Programming1", "Programming2", "Programming3"]
    marks = Marks = [50, 80, 35, 70, 62, 15]
    print(print_modules(modules, marks))

    # 2.2
    modules = ["Calculus1", "Calculus2", "Calculus3", "Programming1", "Programming2", "Programming3"]
    marks = Marks = [50, 80, 35, 70, 62, 15]
    print(print_modules_classification(modules, marks))

    # 3.1
    x = 'alpha077beta123gamma7345738*£$&%(£%£%&(0'
    assert get_digit_sequences_from_string(x) == '077\n123\n7345738\n0\n'
