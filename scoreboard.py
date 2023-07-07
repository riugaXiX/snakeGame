from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(180, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:  {self.score} Highscore: {self.highscore}",
                   align="center", font=("Arial", 16, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()
