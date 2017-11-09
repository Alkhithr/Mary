
import string


class TextToList:
    def __init__(self, string_input=''):
        self.values = []
        for s in string_input:
            self.values.append(s)


def hack_vigenere_attempt():
    alphabet = TextToList(string.ascii_lowercase)
    plaintext = TextToList('symmetric')
    ciphertext = TextToList('beccmlxpcsfynxplac')
    output_left = []
    output_right = []

    # iterate through the plaintext values
    for p in range(0, len(plaintext.values)):
        # iterate through an alphabet length to try figure out what the key is
        for k in range(0, 25):
            # plaintext
            p_index = p
            p_char = plaintext.values[p_index]
            # plaintext char index in alphabet
            a_of_p_index = alphabet.values.index(p_char)
            # key
            k_index = k
            k_char = alphabet.values[k_index]
            # cipher: change the index to 'align'
            c_index = p + 0
            c_char = ciphertext.values[c_index]
            # cipher char index in alphabet
            a_of_c_index = alphabet.values.index(c_char)

            if (a_of_p_index + k_index) % 26 == a_of_c_index:

                output_left.append('({} + {}) mod 26 = {} mod 26 = {}'.format(
                    a_of_p_index, k_index, a_of_p_index + k_index, (a_of_p_index + k_index) % 26))
                output_right.append('{}({}) = {}'.format(alphabet.values[a_of_p_index], k_char, c_char))

    for index in range(0, len(output_left)):
        a = str(output_left[index])
        b = str(output_right[index])
        fixed_length = 40 - len(a)
        print(a, ' ' * fixed_length, b)


if __name__ == '__main__':
    hack_vigenere_attempt()

