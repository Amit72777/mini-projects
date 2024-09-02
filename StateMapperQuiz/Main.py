import tkinter
from turtle import *
import pandas as pd


def ScoreBord(correct):
    """ print score in screen"""
    x = 40.0
    y = -120.0

    tim = Turtle()
    tim.hideturtle()
    tim.penup()
    tim.pensize(10)
    tim.goto(x,y)

    result = f"Your correct answer = {correct} \nYour wrong answer = {30-correct}"
    tim.write(result,font=('Arial', 20, "bold"))


def quiz_game():
    file = pd.read_csv("india_state.csv")
    data = file['state'].to_list()
    #  load data
    cnt = 0
    while cnt <= 29:
        try:
            # input gesss state
            gess_state = screen.textinput(title=f"({cnt}/30)Submission",
                                          prompt="Enter the state name").title().strip()
            gess_state = gess_state.strip()
        except:
            ScoreBord(30-len(data))
            break

        if gess_state == "Exit":
            missingstate = [state for state in data if state not in gess_state]
            new_data = pd.DataFrame(missingstate)
            new_data.to_csv('stateToLearn.csv')
            ScoreBord(30 - len(data))
            break
        if gess_state in data:
            data_row = file[gess_state == file.state]
            x_value = data_row.x
            y_value = data_row.y
            x = int(x_value)
            y = int(y_value)
            tk = Turtle()
            tk.hideturtle()
            tk.penup()
            tk.goto(x, y)
            tk.dot(5, 'red')
            tk.write(gess_state, align="center", font=("Arial", 8, 'bold'))
            data.remove(gess_state)
        cnt += 1

    missingstate = [state for state in data]
    new_data = pd.DataFrame(missingstate)
    new_data.to_csv('stateToLearn.csv')
    ScoreBord(30 - len(data))


def exit_game():
    screen.bye()


tom = Turtle()
tom.tilte("StateMapperQuiz")
screen = Screen()

screen.listen()

screen.addshape("Map.gif")
tom.shape("Map.gif")


# Set up tkinter and buttons
tk_root = screen.getcanvas().winfo_toplevel()  # Get the root tkinter window from the Turtle screen

start_button = tkinter.Button(tk_root, text="Start", command=quiz_game)
start_button.pack(side=tkinter.LEFT, padx=20, pady=20)

exit_button = tkinter.Button(tk_root, text="Exit", command=exit_game)
exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)

screen.mainloop()
