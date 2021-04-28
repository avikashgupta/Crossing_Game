import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_manager = CarManager()

sb = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision
    for car in car_manager.allcars:
        if car.distance(player) < 20:
            game_is_on = False
            sb.game_over()

    # Detect successful crossing
    if player.finish():
        player.go_start()
        car_manager.speed_up()
        sb.increase_level()

screen.exitonclick()
