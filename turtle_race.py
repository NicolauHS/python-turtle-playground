from turtle import Turtle, Screen, textinput
from random import randint

turtle_list = []
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

screen = Screen()
screen.setup(width=500, height=400)

user_bet = textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")

if user_bet:
    is_race_on = True

def finish_race(winner):
    if user_bet.lower() == winner:
        print("You've won!")
    else:
        print("You've lost. Better luck next time...")

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=-105+turtle_index*30)
    turtle_list.append(new_turtle)

while is_race_on:
    for turtle in turtle_list:
        turtle.forward(randint(3, 10))
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.color()[0]
            print(f"the {winning_color} turtle won")
            finish_race(winner=winning_color)

screen.exitonclick()