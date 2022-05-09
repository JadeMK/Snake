from turtle import Turtle
FONT = ("Courier", 22, "normal")
COLOUR = "white"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        # Retrieve saved high score from score.txt
        with open("score.txt") as score:
            self.high_score = int(score.read())
        self.lives = 3
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color(COLOUR)
        self.update_score()

    # Update the scoreboard (clear & write)
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.current_score} | High Score: {self.high_score} | Snake: {self.lives}",
                   move=False, align="center", font=FONT)

    # Score track
    def increase_score(self):
        self.current_score += 1
        self.update_score()

    # Set the high score and update
    def reset_score(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("score.txt", mode="w") as score:
                score.write(str(self.current_score))
        self.current_score = 0
        self.update_score()

    # Write "Game over" on screen
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)
