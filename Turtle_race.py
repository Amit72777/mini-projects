from turtle import Turtle, Screen
import random


def set_position(racer, position):
    """set a position and increase size  of turtle"""
    global color_no
    racer.shapesize(3, 3, 3)
    racer.penup()
    racer.goto(x=-750, y=position)

    racer.color(color_turtle[color_no])
    color_no += 1


screen = Screen()
screen.title("Wellcome to turtle Race Game")
screen.setup(width=1525, height=860)

# TODO 1 : Create a  Turtle object of evey racer

all_turtle = []
for _ in range(6):
    tim = Turtle(shape='turtle')
    all_turtle.append(tim)

# TODO 2 : Create Start and finish line

cross_line = Turtle()
cross_line.pensize(5)

cross_line.penup()
cross_line.goto(-720, 350)
cross_line.setheading(270)
cross_line.pendown()
cross_line.forward(600)

cross_line.penup()
cross_line.goto(720, 350)
cross_line.setheading(270)
cross_line.pendown()
cross_line.forward(600)

# TODO 3: add color and set a position of turtle racer

color_turtle = ['red', 'yellow', 'green', 'blue', 'purple', 'orange']
color_no = 0

y_coordinate = 300
for turtle_racer in all_turtle:
    set_position(turtle_racer, position=y_coordinate)
    y_coordinate -= 100

user_bet = screen.textinput(prompt="Make your bet", title="Which turtle will win the racer? Enter a color:").lower()

# TODO 4: using code all racer a run and go to a finish line
while True:
    tk = random.choice(all_turtle)
    step = random.randint(0, 30)
    tk.forward(step)

    if tk.position() > (750, 350):
        t = Turtle()
        t.hideturtle()
        if user_bet == tk.pencolor():
            t.write("Congratulations 🎉\n You  are winner", align="left", font=("Arial", 20, "bold"))
        else:
            t.write(f"  You are Loss 😔\n {tk.pencolor()} turtle is win", align="left", font=("Arial", 20, "bold"))
        break

screen.exitonclick()
