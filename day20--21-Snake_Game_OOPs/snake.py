from turtle import Turtle, Screen

START_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for pos in START_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        seg=Turtle("square")
        seg.color("white")
        seg.penup()
        seg.goto(pos)
        self.segments.append(seg)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1): # Start, stop and step index 
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:

            self.segments[0].setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:

            self.segments[0].setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:

            self.segments[0].setheading(RIGHT)


        
