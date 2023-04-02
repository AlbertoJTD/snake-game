from turtle import Screen
from snake import Snake
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game 🐍')
screen.tracer(0)

# Snake controls
snake = Snake()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.15)

    snake.move()

screen.exitonclick()
