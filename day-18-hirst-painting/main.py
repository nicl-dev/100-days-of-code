import turtle
import random

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fast")
turtle.colormode(255)
x = -350
y = -300
filtered_colors = [(43, 104, 170), (233, 206, 115), (227, 152, 86), (186, 47, 75), (118, 88, 48), (230, 118, 145),
                   (110, 109, 188), (214, 61, 79), (54, 177, 113), (115, 185, 138), (122, 177, 213), (198, 18, 41),
                   (115, 170, 36), (33, 57, 113), (220, 53, 47), (26, 142, 109), (181, 168, 224), (155, 223, 193),
                   (29, 163, 173), (84, 35, 39), (33, 45, 82), (231, 168, 181), (75, 37, 35), (233, 172, 163),
                   (100, 45, 41), (152, 207, 220)]


def draw_dots(dot_count):
    for _ in range(dot_count):
        tim.forward(60)
        tim.dot(30, random.choice(filtered_colors))


for _ in range(10):
    tim.goto(x, y)
    draw_dots(10)
    y += 60


screen = turtle.Screen()
screen.exitonclick()
