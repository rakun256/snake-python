from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.turtle_x_coordinate = 0
        self.create_snake()

    def create_turtle(self):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("#3C412C")
        new_segment.goto(self.get_coordinate())
        self.segments.append(new_segment)
        return new_segment

    def create_snake(self):
        for s in range(3):
            self.segments.append(self.create_turtle())

    def extend(self):
        self.create_turtle()

    def move(self):
        for seg_num in range (len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def check_direction(self):
        if self.segments[0].heading() == 0:
            return "right"
        elif self.segments[0].heading() == 90:
            return "up"
        elif self.segments[0].heading() == 180:
            return "left"
        elif self.segments[0].heading() == 270:
            return "down"

    def get_coordinate(self):
        if not self.segments:
            return 0, 0

        last_segment_x = self.segments[ - 1].xcor()
        last_segment_y = self.segments[ - 1].ycor()

        if self.check_direction() == "right":
            return last_segment_x - 20, last_segment_y
        elif self.check_direction() == "up":
            return last_segment_x, last_segment_y - 20
        elif self.check_direction() == "left":
            return last_segment_x + 20, last_segment_y
        elif self.check_direction() == "down":
            return last_segment_x, last_segment_y + 20