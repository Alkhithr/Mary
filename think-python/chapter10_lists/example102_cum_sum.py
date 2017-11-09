# Write a function called cumsum that takes a list of numbers and returns the cumulative sum;
# that is, a new list where the ith element is the sum of the first i+1 elements from the original list. For example:
#


def cum_sum(number_list):

    cum_list = []
    for i in range(len(number_list)):
        cum_list.append(sum(number_list[:i]))

    return cum_list


def main():

    number_list = [1, 2, 4, 8, 16, 32]
    print(cum_sum(number_list))


if __name__ == '__main__':
    main()
