from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("SeaGreen")
screen.title("Snaky Snaky")
# tracer = 0 meaning off
screen.tracer(0)

# Snake, food, scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Snake control
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game play loop
while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        snake.reset_snake()
        scoreboard.lives -= 1
        scoreboard.update_score()

    # Detect collision with its tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.lives -= 1
            scoreboard.update_score()
            snake.reset_snake()

    # When the snake eats food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.current_score += 1
        scoreboard.update_score()

    # Game over when all lives run out
    if scoreboard.lives == 0:
        scoreboard.game_over()
        break

screen.exitonclick()
