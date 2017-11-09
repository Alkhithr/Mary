def calc_total(a_list):

    total = 0
    for n in a_list:
        total += n

    return total


def main():

    total_list = []

    while True:
        number = int(input("Give me a number: "))

        if number != 999:
            total_list.append(number)
        elif number == 999:
            break

    print('The sum so far is: {}'.format(calc_total(total_list)))


main()
