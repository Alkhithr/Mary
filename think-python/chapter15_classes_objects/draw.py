import turtle
import time


class Point:
    """"""


class Rectangle:
    """"""


class Circle:
    """"""


point = Point
point.x = 0
point.y = 0


rectangle = Rectangle
rectangle.x = 200
rectangle.y = 100

circle = Circle
circle.radius = 100


rec = turtle.Turtle()
rec.goto([point.x, point.y])

rec.circle(circle.radius)

rec.goto([point.x, point.y])

for i in range(0, 2):
    rec.fd(rectangle.x)
    rec.lt(90)
    rec.fd(rectangle.y)
    rec.lt(90)

time.sleep(20)
