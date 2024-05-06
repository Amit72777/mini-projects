import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from boundry import Boundary

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
border = Boundary('pink')

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collide with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        game_is_on = False
        score.game_over()

    if not snake.snake_collision():
        game_is_on = False
        score.game_over()


screen.exitonclick()
