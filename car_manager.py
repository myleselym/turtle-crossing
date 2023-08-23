from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 45


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.speed(1)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.goto(300, randint(-230, 200))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(MOVE_INCREMENT)









