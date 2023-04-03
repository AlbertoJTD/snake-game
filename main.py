from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game 🐍')
screen.tracer(0)

# Snake & food objects
snake = Snake()
food = Food()
score = ScoreBoard()

# Snake controls
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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_food_position()
        score.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over = True
        score.end_game()



screen.exitonclick()
