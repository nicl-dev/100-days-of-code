import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.shape("turtle")
colors = ["dark orange", "deep sky blue", "indigo", "crimson"]
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


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
        tim.color(random_color())
        direction = random.choice(directions)
        tim.setheading(direction)
        tim.forward(30)


random_walk()

screen = t.Screen()
screen.exitonclick()
