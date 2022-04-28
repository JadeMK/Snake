from turtle import Screen
from snake import Snake

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("SeaGreen")
screen.title("Snaky Snaky")

# Snake
snake = Snake()

# Snake control
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Snake movement test loop
while True:
    snake.move()

screen.exitonclick()