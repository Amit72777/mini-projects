import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # self.food1 = Turtle()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color('blue')
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)


