# Write a definition for a class named Circle with attributes center and radius,
# where center is a Point object and radius is a number.
#
# Instantiate a Circle object that represents a circle with its center at (150,100) and radius 75.
#
# Write a function named point_in_circle that takes a Circle and a Point and
# returns True if the Point lies in or on the boundary of the circle.
#
# Write a function named rect_in_circle that takes a Circle and a Rectangle and returns True
# if the Rectangle lies entirely in or on the boundary of the circle.
#
# Write a function named rect_circle_overlap that takes a Circle and a Rectangle and returns True
# if any of the corners of the Rectangle fall inside the circle.
# Or as a more challenging version, return True if any part of the Rectangle falls inside the circle.


class Point:
    """"""

class Circle:
    """"""

class Rectangle:
    """"""


def point_in_circle(circle, point):
    result = False
    min_point = min([point.x, point.y])
    if circle.radius >= min_point:
        result = True
    return result


# this assumes that the center point is identical for both shapes
def rect_in_circle(rectangle, circle):
    result = False
    max_point = max([rectangle.x, rectangle.y])
    if circle.radius >= max_point:
        result = True
    return result


def rect_circle_overlap(rectangle, circle):
    result = False
    max_point = max([rectangle.x, rectangle.y])
    if circle.radius <= max_point:
        result = True
    return result


def test():

    point = Point
    circle = Circle
    point.x = 150
    point.y = 100

    circle.point = point
    circle.radius = 75

    assert point_in_circle(circle, point) is False

    point.x = 76
    point.y = 75

    assert point_in_circle(circle, point) is True

    rectangle = Rectangle
    rectangle.x = 10
    rectangle.y = 11


if __name__ == '__main__':
    test()

