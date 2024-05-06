from turtle import Turtle


class Boundary(Turtle):
    def __init__(self, boundary_color):
        Turtle.__init__(self)
        self.hideturtle()
        self.color(boundary_color)
        self.penup()
        self.pensize(10)
        self.goto(x=299, y=299)
        self.pendown()
        for _ in range(4):
            self.right(90)
            self.forward(595)

