from turtle import Turtle as t, Screen as scr
from random import choice as c

pen = t()
pen.shape('arrow')
pen.width(10)
color_list = ('CornFlowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen')
directions = (0, 90, 180, 270)

pen.speed(0)

def walk_to_random_direction():
    pen.forward(20)
    pen.color(c(color_list))
    pen.setheading(c(directions))

for i in range(300):
    walk_to_random_direction()

screen = scr()
screen.exitonclick()
