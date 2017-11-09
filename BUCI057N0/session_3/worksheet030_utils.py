import random


def create_random_list(element_count):
    random_list = [0]
    odd = True
    while element_count > 0:
        random_int = random.randint(-128, 128)
        if odd:
            random_int = -1 * random_int
        odd = not odd
        random_list.append(random_int)
        element_count -= 1
    return random_list




