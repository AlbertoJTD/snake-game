from turtle import Turtle

INITIAL_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
STEPS = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

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

        self.segments[0].forward(STEPS)
