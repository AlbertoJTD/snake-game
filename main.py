from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game 🐍')
screen.tracer(0)

initial_positions = [(0,0), (-20, 0), (-40, 0)]
segments = []

for position in initial_positions:
    new_segment = Turtle(shape='square')
    new_segment.penup()
    new_segment.color('white')
    new_segment.goto(position)
    segments.append(new_segment)

game_over = False

while not game_over:
    screen.update()
    time.sleep(1)

    for position in range(len(segments) - 1, 0, -1):
        print('xy position: ', segments[position].position())
        print('xy position - 1: ',segments[position - 1].position())
        print('position: ', position)
        print('position - 1: ',position - 1)
        xy_position = segments[position - 1].position()
        segments[position].goto(xy_position)
        print(f'new position: {segments[position].position()}\n')

    segments[0].forward(20)
    #segments[0].left(90)


screen.exitonclick()
