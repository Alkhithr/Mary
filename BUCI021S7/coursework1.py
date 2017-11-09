# The below has run successfully on IDLE @ cspc700.dcs.bbk.ac.uk
# Uncomment the exec functions at the end to execute each exercise


def get_list_input():
    """input is separated in order to facilitate
    the testing of the functions that do the actual work
    plus it abides by the Don't Repeat Yourself principle
    since this is used multiple times throughout"""
    element_count = int(input('Please enter number of list elements: '))
    input_list = []
    for i in range(0, element_count):
        e = int(input('Please enter element {}: '.format(i+1)))
        input_list.append(e)
    return input_list


def list_contains(A, order_type, items_list=[1, 2, 3]):
    items_input = A
    items_present = []
    result = 'YES'

    if order_type == '1.1':
        for n in items_input:
            if items_list.count(n) > 0:
                if items_present.count(n) == 0:
                    items_present.append(n)
        items_present.sort()
        if items_present != items_list:
            result = 'NO'

    elif order_type == '1.2':
        for n in items_input:
            if items_list.count(n) > 0:
                items_present.append(n)

        if len(items_present) < len(items_list):
            result = 'NO'
        elif len(items_present) == len(items_list):
            if items_present != items_list:
                result = 'NO'
        elif len(items_present) > len(items_list):
            for i in range(0, len(items_present) - len(items_list) + 1):
                items_present_slice = items_present[i:len(items_list) + i]
                if items_present_slice != items_list:
                    result = 'NO'
                else:
                    result = 'YES'
                    break
        else:
            print('You should never get here')

    elif order_type == '1.3':
        if len(items_input) < len(items_list):
            result = 'NO'
        elif len(items_input) == len(items_list):
            if items_input != items_list:
                result = 'NO'
        elif len(items_input) > len(items_list):
            for i in range(0, len(items_input) - len(items_list) + 1):
                items_input_slice = items_input[i:len(items_list) + i]
                if items_input_slice != items_list:
                    result = 'NO'
                else:
                    result = 'YES'
                    break

    return result


def exec_list_contains(order_type):
    """order_type is the coursework exercise number
    1.1 = List containing the given set of elements
    1.2 = List containing the given set of elements in the given order
    1.3 = Lists containing the given set of elements consecutively and in the given order"""
    input_list = get_list_input()
    result = list_contains(input_list, order_type)
    print(result)


def get_string_input():
    """input is separated in order to facilitate
    the testing of the functions that do the actual work
    plus it abides by the Don't Repeat Yourself principle
    since this is used a couple of times"""
    string_input = input('Please enter string: ')
    return string_input


def count_brackets(bracket_input):
    left_bracket_count = 0
    right_bracket_count = 0
    for bracket in bracket_input:
        if bracket == '(':
            left_bracket_count += 1
        elif bracket == ')':
            right_bracket_count += 1
        else:
            pass
    return [left_bracket_count, right_bracket_count]


def math_brackets(string_input):
    result = 'NO'
    left_bracket_count = 0
    right_bracket_count = 0

    # exit with NO if the first or last brackets are of the wrong type
    # Placed outside the loop as one won't have to wait
    # for a full iteration when something wrong can be highlighted immediately
    if string_input[0] == ')' or string_input[len(string_input)-1] == '(':
        return result
        exit()

    # exit with YES if there is only one set of brackets
    if string_input == '()':
        result = 'YES'
        return result
        exit()

    # for the rest figure out the action based on the number of brackets
    for index in range(0, len(string_input)):
        bracket = string_input[index]
        if bracket == '(':
            left_bracket_count += 1
        elif bracket == ')':
            right_bracket_count += 1
            # after each closed bracket the count of right brackets
            # cannot be greater than the count of left brackets
            if right_bracket_count > left_bracket_count:
                result = 'NO'
                return result
                exit()
        else:
            pass

    if (left_bracket_count + right_bracket_count) % 2 == 0 and left_bracket_count == right_bracket_count:
        result = 'YES'

    return result


def exec_count_brackets():
    bracket_input = get_string_input()
    bracket_count = count_brackets(bracket_input)
    print('Left brackets count: {}\nRight brackets count: {}'.format(bracket_count[0], bracket_count[1]))


def exec_math_brackets():
    bracket_input = get_string_input()
    result = math_brackets(bracket_input)
    print(result)


def run_tests():
    """Please ignore the tests"""
    order_type = '1.1'
    assert list_contains([10, 2, 4, 15, 3, 6, 1], order_type) == 'YES'
    assert list_contains([1, 17, 2, 45], order_type) == 'NO'
    assert list_contains([], order_type) == 'NO'

    order_type = '1.2'
    assert list_contains([45, 1, 5, 2, 77, 3], order_type) == 'YES'
    assert list_contains([45, 1, 3, 77, 2], order_type) == 'NO'
    assert list_contains([3, 2, 1, 2, 3, 4], order_type) == 'YES'
    assert list_contains([3, 3, 2, 2, 1, 2], order_type) == 'NO'
    assert list_contains([], order_type) == 'NO'

    order_type = '1.3'
    assert list_contains([3, 2, 1, 2, 3], order_type) == 'YES'
    assert list_contains([3, 1, 2, 3, 2], order_type) == 'YES'
    assert list_contains([3, 3, 2, 2, 1, 2], order_type) == 'NO'
    assert list_contains([], order_type) == 'NO'

    assert count_brackets('(') == [1, 0]
    assert count_brackets(')') == [0, 1]
    assert count_brackets(')(') == [1, 1]
    assert count_brackets('))((') == [2, 2]
    assert count_brackets('') == [0, 0]

    assert math_brackets('()') == 'YES'
    assert math_brackets('(())()') == 'YES'
    assert math_brackets('(()())') == 'YES'
    assert math_brackets('))(())((') == 'NO'
    assert math_brackets('())(()') == 'NO'
    assert math_brackets('()(())') == 'YES'


if __name__ == '__main__':
    run_tests()
    # exec_list_contains('1.1')
    # exec_list_contains('1.2')
    # exec_list_contains('1.3')
    # exec_count_brackets()
    # exec_math_brackets()
