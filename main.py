from turtle import Screen
import time
from scoreboard import Scoreboard
from screen_draw import ScreenDraw
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width = 700, height = 700)
screen.bgcolor("#a8c64e")
screen.title("Snake Game Python")
screen.tracer(0)

score = 0
high_score = 0
snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.show_board(score)
screen_draw = ScreenDraw()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.left,"a")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) <15:
        score += 1
        food.refresh()
        snake.extend()
        scoreboard.show_board(score)

    if snake.segments[0].xcor() > 300 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -300:
        score = 0
        scoreboard.show_board(score)
        snake.reset()

    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            score = 0
            scoreboard.show_board(score)
            snake.reset()

screen.exitonclick()