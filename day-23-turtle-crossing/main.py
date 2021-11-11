import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.listen()
player = Player()
screen.onkeypress(player.move, "w")
car_manager = CarManager()

game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    car_manager.move_cars()
    screen.update()
    loop_count += 1
    if loop_count % 12 == 0:
        car_manager.spawn_car()


screen.exitonclick()
