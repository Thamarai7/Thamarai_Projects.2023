from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

Up = 90
Down = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.move = 20
        self.head = self.segment[0]

    def create_snake(self):
        for position in starting_positions:
            new_segment = Turtle("square")
            # new_segment.shapesize(100)
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segment.append(new_segment)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            x = self.segment[seg_num - 1].xcor()
            y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(x, y)
        self.head.forward(self.move)

    def up(self):
        if self.head.heading() != Down:
            self.segment[0].setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)
