from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_coords = [(0, 0), (-20, 0), (-40, 0)]
segments = []

def render_snake():
    for position in snake_coords:
        square = Turtle("square")
        square.color("white")
        square.up()
        square.goto(position)
        segments.append(square)
        print(segments)
    
def set_direction(direction):
    # print(segments[0].heading())
    head = segments[0]
    heading = head.heading()
    match direction:
        case 'right':
            if int(heading) is not 180:
                head.setheading(0)
        case 'left':
            if int(heading) is not 0:
                head.setheading(180)    
        case 'up':
            if int(heading) is not 270:
                head.setheading(90)
        case 'down':
            if int(heading) is not 90:
                head.setheading(270)

screen.listen()

# EVENT LISTENERS #################################
screen.onkey(key="Down",  fun=lambda: set_direction('down'))
screen.onkey(key="Left",  fun=lambda: set_direction('left'))
screen.onkey(key="Up",    fun=lambda: set_direction('up'))
screen.onkey(key="Right", fun=lambda: set_direction('right'))

is_game_on = True

render_snake()
screen.update()
while is_game_on:
    screen.update()
    time.sleep(0.5)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    
screen.exitonclick()