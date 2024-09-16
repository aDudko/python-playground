from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "tan"]
user_bet = screen.textinput(title="Make your bet", prompt=f"Witch turtle will win the race? Enter a color\n{colors}: ")
turtles = []

for turtle_index in range(7):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=(-90 + (turtle_index * 30)))
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} turtle is the winner!")
            else:
                print(f"You've lost! The {win_color} turtle is the winner!")
        turtle_speed = random.randint(0, 10)
        turtle.forward(turtle_speed)

screen.exitonclick()
