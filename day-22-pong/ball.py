from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + 0.033
        new_y = self.ycor() + 0.033
        self.setpos(new_x, new_y)
