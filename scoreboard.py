from turtle import Turtle
FONT = ("Courier", 22, "normal")
COLOUR = "white"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.lives = 3
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color(COLOUR)
        self.update_score()

    # Update the scoreboard (clear & write)
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.current_score} | Snake: {self.lives}", move=False, align="center", font=FONT)

    # Write "Game over" on screen
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)
