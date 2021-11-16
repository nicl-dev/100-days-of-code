from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        car = Turtle("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(choice(COLORS))
        car.setpos(340, randint(-250, 250))
        self.cars.append(car)

    def move_cars(self):
        for car in range(len(self.cars)):
            new_x = self.cars[car].xcor() - self.speed
            new_y = self.cars[car].ycor()
            self.cars[car].goto(new_x, new_y)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
