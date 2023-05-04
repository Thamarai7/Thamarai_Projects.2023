import turtle
from turtle import Turtle, Screen
import random

s = Screen()
s.setup(width=500, height=400)


def Race_line():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(230, 100)
    turtle.pendown()
    turtle.setheading(180)
    turtle.setheading(90)
    turtle.goto(230, -100)

Race_line()
# Make a user guess
user = s.textinput(title="Make your bet", prompt="Which Turtle will win the race?")
# colors for turtle
colors = ["red", "orange", "yellow", "green", "purple", "blue"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    t = turtle.Turtle(shape="turtle")
    # Give a color for each turtle by using loop as a index of color list
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-230, y=y_position[turtle_index])
    # add all turtle instance to the list,beacuse we want to run it
    all_turtles.append(t)

print(all_turtles)
if user:
    is_race = True

while is_race:
    # Run through the turtle list and move each turtle
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race = False
            turtle_color = t.pencolor()
            if user == turtle_color:
                print(f"you've win,{turtle_color} is winning Turtle")
            else:
                print(f"You've wrong,{turtle_color} is win")
        #  Taking random distance to move each turtle
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

s.exitonclick()
