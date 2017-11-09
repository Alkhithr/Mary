def right_justify(s):
    spaces_to_add = 70 - len(s)
    print(' ' * spaces_to_add, s)


def do_something():
    print('Doing something')


def do_twice(function_name):
    function_name()
    function_name()


def do_twice_v2(function_name, function_value):
    function_name(function_value)
    function_name(function_value)


# 4. Copy the definition of print_twice from earlier in this chapter to your script.
def print_twice(a):
    print(a)
    print(a)


def do_four(function_name, function_value):
    for i in range(0, 4):
        function_name(function_value)


def main():

    # 1. Write a function named right_justify that takes a string named s as a parameter
    # and prints the string with enough leading spaces so that the last letter of the
    # string is in column 70 of the display
    right_justify('monty')

    # 2. A function object is a value you can assign to a variable or pass as an argument.
    # For example, do_twice is a function that takes a function object as an argument
    # and calls it twice:
    do_twice(do_something)

    # 3. Modify do_twice so that it takes two arguments, a function object and a value,
    # and calls the function twice, passing the value as an argument.
    do_twice_v2(right_justify, 'rightfully twice')

    # 5. Use the modified version of do_twice to call print_twice twice, passing 'spam'
    # as an argument.
    do_twice_v2(print_twice, 'spam')

    # 6. Define a new function called do_four that takes a function object and a value and
    # calls the function four times, passing the value as a parameter. There should be
    # only two statements in the body of this function, not four.
    do_four(right_justify, 'I am Six')


main()
