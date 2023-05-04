import turtle
from turtle import Turtle,Screen
t = Turtle()
import random
# def draw_shape(num_side):
#     angle = 360/num_side
#     for _ in range(num_side):
#         t.forward(100)
#         t.left(angle)
# for shape_in in range(3, 11):
#     draw_shape(shape_in)
#
directions =[0, 90, 180, 360]
t.pensize(5)
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b =  random.randint(0, 255)
    rand = (r, g, b)
    return rand
t.speed("fastest")
# for _ in range(200):
#     t.color(random_color())
#     t.forward(10)
#     t.setheading(random.choice(directions))
# def draw_spirograph(size_of_gap):
#     for i in range(int(360 / size_of_gap)):
#         t.color(random_color())
#         t.circle(100)
#         t.setheading(t.heading() + size_of_gap)
#
# draw_spirograph(5)
# def draw_square(shape):
#     for _ in range (int(360 / shape)):
#         t.color(random_color())
#         t.forward(50)
#         t.right(90)
#         t.setheading( t.heading() + shape)
#         t.forward(50)
#         t.right(90)
# draw_square(5)

s = Screen()
s.exitonclick()
