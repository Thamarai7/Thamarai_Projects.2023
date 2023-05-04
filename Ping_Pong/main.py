import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Pong")
s.tracer(0)

r_paddle = Paddle((380, 15))
l_paddle = Paddle((-380, -10))
ball = Ball()
score = Score()

s.listen()
s.onkey(r_paddle.go_up, "Up")
s.onkey(r_paddle.go_down, "Down")

s.onkey(l_paddle.go_up, "w")
s.onkey(l_paddle.go_down, "s")


is_on = True
while is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    if  ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 381:
        ball.reset()
        score.score_l()
    if ball.xcor() < -381:
        ball.reset()
        score.score_r()

s.exitonclick()
