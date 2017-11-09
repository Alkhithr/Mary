import turtle


def square(bob, length):

    for x in range(4):
        bob.fd(length)
        bob.lt(90)


def polygon(t, length, n):

    angle = 360 / n

    for x in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):

    n = 360
    length = r / n

    polygon(t, length, n)


def arc(t, r, angle):

    length = r / angle

    polygon(t, length, angle)


def main():

    bob = turtle.Turtle()
    length = 50
    sides = 12

    # square(bob, length)
    # polygon(bob, length, sides)

    circumference = length * sides

    # circle(bob, circumference)
    arc(bob, circumference, sides)

    turtle.mainloop()


main()
