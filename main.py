import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_generator = CarManager()
scoreboard = Scoreboard()

screen.listen()
if screen.onkey(player.move_up, "Up"):
    screen.update()


def turtle_crossing():
    game_is_on = True
    while game_is_on:
        time.sleep(.1)
        screen.update()
        car_generator.create_car()
        car_generator.move_cars()

        if player.ycor() > 230:
            screen.update()
            scoreboard.increase_level()
            player.player_reset()

        for car in car_generator.all_cars[1:]:
            if player.distance(car) < 22:
                game_is_on = False
                scoreboard.game_over()


turtle_crossing()


screen.exitonclick()
