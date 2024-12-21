import turtle as t
from math import degrees, pi
from random import randint

pen = t.Turtle()
pen.shape('classic')
pen.speed('fastest')
t.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

def spirograph(angle, size, circle_size=50):
    for _ in range(int(360/angle)):
        pen.color(random_color())
        pen.forward(size)
        pen.setheading(pen.heading() - angle)
        pen.down()
        pen.circle(circle_size)
        pen.up()

spirograph(5, 0, 100)


screen = t.Screen()
screen.exitonclick()