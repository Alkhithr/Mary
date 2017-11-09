# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +


def draw_grid():
    row_line = '+ - - - - + - - - - +'
    column_line = '|         |         |'
    for i in range(0, 11):
        if i in (0, 5, 10):
            print(row_line)
        else:
            print(column_line)


# Write a function that draws a similar grid with four rows and four columns.

def ends_with(value, max_value):

    if value != max_value:
        output = ''
    else:
        output = '\n'

    return output


def draw_row_type(row_type, cell_width, cell_count):

    edge_symbol = ''
    line_symbol = ''
    column_range = cell_count * cell_width + 1

    if row_type.lower() == 'solid':

        edge_symbol = '+ '
        line_symbol = '- '

    elif row_type.lower() == 'columns':

        edge_symbol = '| '
        line_symbol = '  '

    for index in range(0, column_range):
        ew = ends_with(index, column_range)
        if index == 0 or index % cell_width ==0:
            print(edge_symbol, end=ew)
        else:
            print(line_symbol, end=ew)


def draw_grid_v2(row_count, cell_count):

    cell_width = 5
    row_height = 5
    row_range = row_count * row_height + 1

    for row_number in range(0, row_range):

        if row_number == 0 or row_number % cell_width == 0:

            draw_row_type('solid', cell_width, cell_count)

        else:

            draw_row_type('columns', cell_width, cell_count)

        print()


def main():

    print('\n\ndraw grid version 1\n\n')
    draw_grid()

    print('\n\ndraw grid version 2\n\n')
    draw_grid_v2(4, 4)


main()
