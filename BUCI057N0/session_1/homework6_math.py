# Write a program that shows the use of all 7 math functions
# A bit unsure what "all" the 7 math functions are but here's a bit of math anyway

import random as rand
import math


def main():

    signal_power = rand.randint(0, 100)
    noise_power = rand.randint(0, 100)
    radians = rand.randint(0, 100)
    degrees = rand.randint(0, 100)
    x = rand.randint(0, 10)
    y = rand.randint(0, 10)
    result = None

    print('signal_power = {}\nnoise_power = {}\nradians = {}\ndegrees = {}\n x = {}\ny = {}'.format(signal_power,
                                                                                                    noise_power,
                                                                                                    radians,
                                                                                                    degrees, x, y))

    cmd_list = ['10 * math.log10(signal_power / noise_power)',
                'math.sin(radians)',
                'degrees / 180.0 * math.pi',
                'x + y',
                'x - y',
                'x * y',
                'x / y',
                'x // y',
                'x % y',
                'math.pow(x,y)']

    for cmd in cmd_list:

        result = eval(cmd)
        print('{} = {}'.format(cmd, result))


main()

