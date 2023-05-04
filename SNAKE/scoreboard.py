from turtle import Turtle
align = "center"
Font =("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()


    def update_score(self):
        self.clear()
        self.write(f"score:{self.score} High Score:{self.high_score}", align=align, font=Font)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt" ,mode="w") as data:
                data.write(f"{self.high_score}")
            self.score = 0
            self.update_score()

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align=align, font=Font)
    def increase_score(self):
        self.score += 1
        self.update_score()