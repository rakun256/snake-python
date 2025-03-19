from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-310, 310)
        self.hideturtle()
        self.high_score = 0
        self.color("#3C412C")

    def show_board(self, score):
        super().clear()
        if score > self.high_score:
            self.high_score = score
        message = f"Your current score is: {score}, Your high score is: {self.high_score}"
        super().write(align="left", move=False, arg=message, font=("Courier", 12, "bold"))
