import turtle as t
from random import choice as c

pen = t.Turtle()
pen.shape('classic')
pen.speed('fastest')
t.colormode(255)


pen.up()
pen.goto(-400,-360)

color_list = [(245, 243, 238), (247, 242, 244), (240, 245, 241), (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),(36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 78, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 189)]

for _ in range(10):
    for _ in range(10):
        pen.down()
        pen.color(c(color_list))
        pen.dot(60)
        pen.up()
        pen.forward(90)
    pen.goto(-400, pen.ycor()+80)    

screen = t.Screen()
screen.exitonclick()
screen.window_width(800)
screen.window_height(800)