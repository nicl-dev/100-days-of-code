from turtle import Turtle


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_parts = []
        for position in self.starting_positions:
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
