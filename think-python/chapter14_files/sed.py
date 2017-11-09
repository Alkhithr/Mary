# Write a function called sed that takes as arguments a pattern string, a replacement string, and two filenames;
# it should read the first file and write the contents into the second file (creating it if necessary).
# If the pattern string appears anywhere in the file, it should be replaced with the replacement string.
#
# If an error occurs while opening, reading, writing or closing files, your program should catch the exception,
# print an error message, and exit. Solution: http://thinkpython2.com/code/sed.py.
#


def sed(pattern, replacement, file_from, file_to):
    fin = open(file_from)
    fout = open(file_to, 'w')

    for line in fin:
        sed_line = line.replace(pattern, replacement)
        fout.write(sed_line)

    fout.close()


if __name__ == '__main__':

    def test_sed():
        fout = open('in.txt', 'w')
        fout.write('I want ice cream')
        fout.close()
        result = ''
        sed('I', 'We', 'in.txt', 'out.txt')
        fin = open('out.txt')
        for line in fin:
            result = line
        return result

    assert test_sed() == 'We want ice cream'
