from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allcars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        chance = random.randint(1,6)
        if chance == 1:
            cars = Turtle("square")
            cars.shapesize(stretch_len=2,stretch_wid=1)
            cars.penup()
            cars.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            cars.goto(300,random_y)
            self.allcars.append(cars)

    def move_cars(self):
        for car in self.allcars:
            car.backward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT


