from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-310, 310)
        self.hideturtle()
        self.color("#3C412C")

    def show_board(self, score):
        message = f"Your current score is: {score}"
        super().clear()
        super().write(align="left", move=False, arg=message, font=("Courier", 15, "bold"))

    def game_over(self, score):
        self.goto(0,0)
        message = f"GAME OVER\nYOUR SCORE IS: {score}"
        super().clear()
        super().write(align="center", move=False, arg=message, font=("Courier", 30, "bold"))

