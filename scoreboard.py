from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.pu()
        self.ht()
        self.goto(-290, 260)
        self.color("black")
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.level} High Score: {self.high_score}", align="left", font=FONT)

    def reset_hs(self):
        if self.level > self.high_score:
            self.high_score = self.level
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.level = 0

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def increment_level(self):
        self.level += 1
        self.clear()
        self.update_score()


