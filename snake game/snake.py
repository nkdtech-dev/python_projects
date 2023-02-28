from turtle import Turtle
COR=[(0,0),(-20,0),(-40,0)]
D=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.tt=[]
        self.create()
        self.h=self.tt[0] 
    def create(self):
        """Create the snake"""
        for i in COR:
            self.addsnake(i)
    def addsnake(self,i):
        """Add the snake length"""
        t=Turtle(shape="square")
        t.color("cyan")
        t.pu()
        t.goto(i)
        self.tt.append(t)
    def reset(self):
        for i in self.tt:
            i.goto(1500,1500)
        self.tt.clear()
        self.create()
        self.h=self.tt[0] 

    def extend(self):
        """Add the snake length"""
        self.addsnake(self.tt[-1].position())

    def move(self):
        """Allows move the snake forward"""
        for n in range(len(self.tt)-1,0,-1):
            nx=self.tt[n-1].xcor()
            ny=self.tt[n-1].ycor()
            self.tt[n].goto(nx,ny)
        self.h.fd(D)
    def up(self):
        """Go up"""
        if self.h.heading()!=DOWN:
            self.h.setheading(UP)
    def down(self):
        """Go down"""
        if self.h.heading()!=UP:
            self.h.setheading(DOWN)
    def left(self):
        """Go left"""
        if self.h.heading()!=RIGHT:
            self.h.setheading(LEFT)
    def right(self):
        """Go right"""
        if self.h.heading()!=LEFT:
            self.h.setheading(RIGHT)