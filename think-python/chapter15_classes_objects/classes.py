class Point:
    """Represents a point in 2-D space."""


def print_point(p):
    print('(%g %g)' % (p.x, p.y))


blank = Point
blank.x = 1
blank.y = 2

print_point(blank)

blank.x = 10

print_point(blank)
