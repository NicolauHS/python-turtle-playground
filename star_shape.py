from turtle import Turtle as t, Screen as scr
from random import choice as c
import time

pen = t()
pen.shape('arrow')

pen.speed(0)

pen.forward(120)

for i in range(36):
    pen.right(190)
    pen.forward(240)
    # time.sleep(.1)

screen = scr()
screen.exitonclick()
