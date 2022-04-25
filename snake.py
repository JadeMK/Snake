from turtle import Turtle
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
COLOUR = "White"


class Snake:

    def __init__(self):
        self.segments = []
        self.new_snake()

    # Create a new snake (3 segments)
    def new_snake(self):
        for position in START_POSITION:
            self.new_segment(position)

    # Create a segment
    def new_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(COLOUR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)