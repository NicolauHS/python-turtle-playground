from turtle import Turtle as t, Screen as scr
from random import choice as c

pen = t()
pen.shape('arrow')
color_list = ['black', 'red', 'blue', 'green', 'yellow', 'deep sky blue', 'lime green', 'dark red', 'dark magenta']

pen.speed(0)
pen.up()
pen.goto(-50, 400)
pen.down()

def draw_shape(sides, side_length, shape_color):
    pen.color(c(color_list))
    pen.pencolor(shape_color)
    for i in range(sides):
        pen.forward(side_length)
        pen.right(360/sides)

for i in range(3, 10):
    print(i%3)
    draw_shape(i, 100, color_list[i%3])

screen = scr()
screen.exitonclick()
