from turtle import Turtle

class ScreenDraw(Turtle):
    def __init__(self):
        super().__init__()
        super().color("#3C412C")
        super().pensize(width=4)
        super().hideturtle()
        super().penup()
        super().goto(-310, 310)
        super().pendown()
        super().forward(620)
        super().right(90)
        super().forward(620)
        super().right(90)
        super().forward(620)
        super().right(90)
        super().forward(620)

