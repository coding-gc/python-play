from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

import os

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.read_file()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
        self.update_file()

    def update_file(self):
        path = './data.txt'
        with open(path, "w") as file:
            file.write(str(self.highscore))

    def read_file(self):
        self.highscore = 0
        path = './data.txt'
        if os.path.isfile(path):
            with open(path, "r") as file_read:
                self.highscore = int(file_read.read())
        # print(self.highscore)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
