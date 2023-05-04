from turtle import Turtle

align = "center"
Font =("Arial", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 270)
        self.write(self.l_score, align=align, font=Font)
        self.goto(100, 270)
        self.write(self.r_score, align=align, font=Font)

    def score_r(self):
        self.r_score += 1
        self.update_score()

    def score_l(self):
        self.l_score += 1
        self.update_score()
