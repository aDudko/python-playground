from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
DATA = "data.txt"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(DATA) as data:
            self.high_score = int(data.read())
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA, mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
