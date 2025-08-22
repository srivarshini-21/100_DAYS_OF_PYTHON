import time
from turtle import Turtle,Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
level=Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")
game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_on=False
            level.game_over()
    # Detect finishline crossing
    if player.finish():
        player.go_to_start()
        car_manager.level_up()
        level.update_level()





screen.exitonclick()