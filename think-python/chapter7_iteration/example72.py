
def eval_loop():

    while True:
        x = input('Type something: ')
        if x != 'done':
            my_eval(x)
        else:
            print('yeeeee')
            my_eval(x)
            break


def my_eval(x):

    try:
    print(eval(x))

def main():

    eval_loop()


main()