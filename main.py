from turtle import Screen
from snake import Snake
from food import Food
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("SeaGreen")
screen.title("Snaky Snaky")
# tracer = 0 meaning off
screen.tracer(0)

# Snake, food
snake = Snake()
food = Food()

# Snake control
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Snake movement test loop
while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        snake.reset_snake()
        # TODO: Update lives

    # When the snake eats food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        # TODO: Update scores

screen.exitonclick()