from turtle import Turtle
from random import choice
P=[-280,-260,-240,-220,-200,-180,-160,-140,-120,-100,-80,-60,-40,-20,0,20,40,60,80,100,120,140,160,180,200,220,240,260,280]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.pu()
        self.color("blue")
        self.speed(0)
        self.refresh()
    def refresh(self):
        """Changes position of food"""
        x=choice(P)
        y=choice(P)
        self.goto(x,y)