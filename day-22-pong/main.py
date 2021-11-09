from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

player1 = Paddle(-350, 0)
player2 = Paddle(350, 0)
screen.onkeypress(player1.go_up, "w")
screen.onkeypress(player1.go_down, "s")
screen.onkeypress(player2.go_up, "Up")
screen.onkeypress(player2.go_down, "Down")

game_on = True

while game_on:
    screen.update()

screen.exitonclick()
