import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("red")
        self.speed("fastest")
        self.refersh()

    def refersh(self):
        random_x = random.randint(-341, 341)
        random_y = random.randint(-220, 220)
        self.goto(random_x, random_y)
