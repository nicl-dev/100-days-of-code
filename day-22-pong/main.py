from turtle import Screen, Turtle


def go_up():
    new_y = player1.ycor() + 20
    player1.goto(x=player1.xcor(), y=new_y)


def go_down():
    new_y = player1.ycor() - 20
    player1.goto(x=player1.xcor(), y=new_y)


paddle1_x = 350
paddle1_y = 0
paddle_width = 5
paddle_len = 1

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")

player1 = Turtle()
player1.speed("fastest")
player1.penup()
player1.shape("square")
player1.color("white")
player1.shapesize(paddle_width, paddle_len)
player1.goto(paddle1_x, paddle1_y)

game_on = True

while game_on:
    screen.update()

screen.exitonclick()
