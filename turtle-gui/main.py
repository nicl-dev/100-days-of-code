import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
colors = ["dark orange", "deep sky blue", "indigo", "crimson"]
directions = [0, 90, 180, 270]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
    num_sides += 1


def random_walk():
    tim.speed("fastest")
    tim.pensize(10)
    for _ in range(1, 500):
        tim.color(random.choice(colors))
        direction = random.choice(directions)
        tim.setheading(direction)
        tim.forward(30)


random_walk()

screen = t.Screen()
screen.exitonclick()
