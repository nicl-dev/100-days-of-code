from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
ball = Ball()
player1 = Paddle(-350, 0)
player2 = Paddle(350, 0)
screen.onkeypress(player1.go_up, "w")
screen.onkeypress(player1.go_down, "s")
screen.onkeypress(player2.go_up, "Up")
screen.onkeypress(player2.go_down, "Down")

game_on = True
while game_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with player1 and player2
    if ball.distance(player2) < 50 and ball.xcor() > 330 or ball.distance(player1) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.p1_point()

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.p2_point()

screen.exitonclick()
