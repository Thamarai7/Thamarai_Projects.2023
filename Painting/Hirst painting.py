import turtle
from turtle import Turtle, Screen
from color_list import color_list
import random

t = turtle.Turtle()
t.speed("fastest")
turtle.colormode(255)
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
num_of_dots = 101

for do_count in range(1, num_of_dots):
    t.dot(20, random.choice(color_list))
    t.forward(50)
    if do_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

s = turtle.Screen()
s.exitonclick()
