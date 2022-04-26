from turtle import Screen
from snake import Snake

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("SeaGreen")
screen.title("Snaky Snaky")

# Snake
snake = Snake()

# Snake movement test loop
while True:
    snake.move()

screen.exitonclick()