from turtle import Turtle
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
COLOUR = "White"
# Turtle starts pointing towards the east and goes counterclockwise
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.new_snake()
        self.head = self.segments[0]

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

    # Snake movement
    def move(self):
        # Segments move starting from the end of the snake
        for position in range(len(self.segments) - 1, 0, -1):
            # get a hold of the position of the next segment
            new_x = self.segments[position - 1].xcor()
            new_y = self.segments[position - 1].ycor()
            self.segments[position].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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

    # Reset the snake
    def reset_snake(self):
        # Dispose of the old snake (out of the current window)
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.new_snake()
        self.head = self.segments[0]

