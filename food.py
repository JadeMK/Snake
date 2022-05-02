from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)  # 10 x 10
        self.color("SpringGreen")
        self.refresh()

    def refresh(self):
        # New food location
        random_x = randint(-200, 200)
        random_y = randint(-200, 200)
        self.goto(random_x, random_y)
