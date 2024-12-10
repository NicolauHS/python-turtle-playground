from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()

pen.speed('fastest')

def reset_screen():
    pen.clear()
    pen.up()
    pen.home()
    pen.down()

def move_forwards():
    pen.forward(10)

def move_backwards():
    pen.back(10)

def turn_to_direction(direction):
    if direction is 'right':
        pen.right(10)
    else:
        pen.left(10)

screen.listen()

# EVENT LISTENERS #################################
screen.onkey(key="Down",  fun=move_backwards)
screen.onkey(key="Left",  fun=lambda: turn_to_direction('left'))
screen.onkey(key="Up",    fun=move_forwards)
screen.onkey(key="Right", fun=lambda: turn_to_direction('right'))
screen.onkey(key="c",     fun=reset_screen)

screen.exitonclick()