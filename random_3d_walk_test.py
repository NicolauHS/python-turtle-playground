from turtle import Turtle as t, Screen as scr, done
from random import choice as c

screen = scr()
screen.setup(width=800, height=600)
screen.title("3D Random Walk")
color_list = ('CornFlowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen')
directions = (0, 90, 180, 270)

point = t()
point.speed(3)  
point.shape('arrow')
point.width(10)

movements = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

x, y, z = 0, 0, 0

def project_3d_to_2d(x, y, z):
    scale = 15
    x2d = x - y
    y2d = (x + y) / 2 - z
    return x2d * scale, y2d * scale

def move_point(dx, dy, dz):
    global x, y, z
    point.color(c(color_list))
    x += dx
    y += dy
    z += dz
    x2d, y2d = project_3d_to_2d(x, y, z)
    point.goto(x2d, y2d)

for _ in range(300):
    move = c(movements)
    move_point(*move)

done()
