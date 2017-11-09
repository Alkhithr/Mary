# If there are 23 students in your class, what are the chances that two of you have the same birthday?
# You can estimate this probability by generating random samples of 23 birthdays and checking for matches.
# Hint: you can generate random birthdays with the randint function in the random module.

import random


def check_birthday(students):

    birthdays = []

    for i in range(students):
        birthdays.append(random.randint(0, 360))

    birthdays.sort()
    return birthdays


def main():

    x = check_birthday(23)
    print(x)


main()
