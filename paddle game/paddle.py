from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,c):
        super().__init__()
        self.create(c)
    def create(self,cor):
        """Creates the paddles and takes"""
        self.shape("square")
        self.pu()
        self.speed(0)
        self.color("white")
        self.shapesize(5,1)
        self.goto(cor,0)
    def moveup(self):
        """Enable motion upward"""
        y=self.ycor()+60
        self.goto(self.xcor(),y)
    def movedown(self):
        """Enable motion downward"""
        y=self.ycor()-60
        self.goto(self.xcor(),y)
    def movein(self):
        """Enable motion inward"""
        pass
        
