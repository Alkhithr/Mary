class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '{},{}'.format(self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            result = self.add_point(other)
        else:
            result = self.sum_tuple(other)
        return result

    def __radd__(self, other):
        return self.__add__(other)

    def add_point(self, other):
        result = Point()
        result.x = self.x + other.x
        result.y = self.y + other.y
        return result

    def sum_tuple(self, other):
        result = Point()
        result.x = self.x + other[0]
        result.y = self.y + other[1]
        return result


def main():
    p1 = Point(1, 1)
    print('point:', p1)

    p2 = Point(2, 3)
    print('point:', p1 + p2)

    p3 = 3, 4
    print('point:', p1 + p3)
    print('point:', p3 + p1)


if __name__ == '__main__':
    main()