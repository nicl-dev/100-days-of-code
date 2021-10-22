from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y = 166
x = -240

for n in range(6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[n])
    tim.goto(x, y)
    y -= 66

screen.exitonclick()
