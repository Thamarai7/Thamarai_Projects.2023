import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

s = Screen()
s.setup(width=600, height=600)
s.tracer(0)
s.listen()

player = Player()
car = CarManager()
score = Scoreboard()
s.onkey(player.go_up, "Up")
s.onkey(player.go_down, "Down")
s.onkey(player.go_right, "Right")
s.onkey(player.go_left, "Left")
# s.onkey()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    s.update()

    car.create_car()
    car.move_cars()

    for c_a_r in car.all_cars:
        if c_a_r.distance(player) < 25:
            game_is_on = False
            score.game_over()
    if player.finish():
        player.go_to_start()
        car.Move_speed()
        player.p_speed()
        score.score()


s.exitonclick()
