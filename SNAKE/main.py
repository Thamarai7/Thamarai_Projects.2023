import time
from turtle import Screen,Turtle
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake")
s.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
is_on = True
while is_on:
    s.update()
    time.sleep(0.3)

    snake.move()

    #Detect the food and count score
    if snake.head.distance(food) < 10:
        food.refresh()
        score.increase_score()

    #Detect  the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

s.exitonclick()
