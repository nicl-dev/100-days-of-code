from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_parts = []

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_part = Turtle(shape="square")
            snake_part.penup()
            snake_part.color("white")
            snake_part.setpos(position)
            self.snake_parts.append(snake_part)

    def move(self):
        for snake_part in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[snake_part - 1].xcor()
            new_y = self.snake_parts[snake_part - 1].ycor()
            self.snake_parts[snake_part].goto(new_x, new_y)
        self.snake_parts[0].forward(20)
