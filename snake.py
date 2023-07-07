import turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
SCREENWIDTH = 800
SCREENHHEIGHT = 600


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for postion in STARTING_POSITION:
            self.new_segment(postion)

    def new_segment(self, position):
        sleepy = turtle.Turtle(shape="square")
        sleepy.color("purple")
        sleepy.penup()
        sleepy.goto(position)
        self.segment.append(sleepy)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def extend(self):
        self.new_segment(self.segment[-1].position())

    def move(self):
        for x in range(len(self.segment)-1, 0, -1):
            new_xcor = self.segment[x-1].xcor()
            new_ycor = self.segment[x-1].ycor()
            self.segment[x].goto(new_xcor, new_ycor)
        self.segment[0].forward(MOVING_DISTANCE)

    def left(self):
        if self.segment[0].heading() == 0 or self.segment[0].heading() == 180:
            pass
        else:
            self.segment[0].setheading(180)

    def up(self):
        if self.segment[0].heading() == 90 or self.segment[0].heading() == 270:
            pass
        else:
            self.segment[0].setheading(90)

    def right(self):
        if self.segment[0].heading() == 0 or self.segment[0].heading() == 180:
            pass
        else:
            self.segment[0].setheading(0)

    def down(self):
        if self.segment[0].heading() == 90 or self.segment[0].heading() == 270:
            pass
        else:
            self.segment[0].setheading(270)


class Sscreen:

    def __init__(self):
        self.screen1 = turtle.Screen()
        self.setup_screen()

    def setup_screen(self):
        self.screen1.setup(width=SCREENWIDTH, height=SCREENHHEIGHT)
        self.screen1.bgcolor("Black")
        self.screen1.bgcolor("#7B3F00")
        self.screen1.title("Snake Game")
        self.screen1.tracer(0)
