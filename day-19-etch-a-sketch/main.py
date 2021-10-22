from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def clockwise():
    tim.right(10)


def counter_clockwise():
    tim.left(10)


screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backwards)
screen.onkeypress(key='d', fun=clockwise)
screen.onkeypress(key='a', fun=counter_clockwise)
screen.onkeypress(key='c', fun=tim.reset)
screen.onkeypress(key='Escape', fun=screen.bye)

screen.listen()
screen.title("Etch-A-Sketch!")
screen.exitonclick()
