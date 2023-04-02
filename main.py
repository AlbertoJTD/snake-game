from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game 🐍')
screen.tracer(0)

snake = Snake()
game_over = False

while not game_over:
    screen.update()
    time.sleep(1)

    snake.move()

screen.exitonclick()
