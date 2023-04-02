from turtle import Turtle

# Initial setup
INITIAL_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
STEPS = 20

# Directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in INITIAL_POSITIONS:
            new_segment = Turtle(shape='square')
            new_segment.penup()
            new_segment.color('white')
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for position in range(len(self.segments) - 1, 0, -1):
            xy_position = self.segments[position - 1].position()
            self.segments[position].goto(xy_position)

        self.head.forward(STEPS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

