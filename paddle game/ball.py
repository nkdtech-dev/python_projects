from turtle import Turtle
from random import randint
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create()
    def create(self):
        """Create the ball"""
        self.shape("circle")
        self.color("blue")
        self.speed(0)
        self.pu()
        self.xx=10
        self.yy=10
        self.ms=0.1
    def move(self):
        """Changes direction every refresh"""
        x=self.xcor()+self.xx
        y=self.ycor()+self.yy
        self.goto(x,y)
    def bounwall(self):
        """Change direction when bounce on wall"""
        self.yy*=-1
    def bounpad(self):
        """Change direction when bounce on paddle"""
        self.xx*=-1
        self.ms-=0.01
    def refresh(self):
        self.goto(0,0)
        self.ms=0.1
        self.bounpad()