from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.ls=0
        self.rs=0
        self.upscore()
    def upscore(self):
        self.clear()
        self.goto(-100,290)
        self.write(self.ls,False,"center",("Courier",60,"bold"))
        self.goto(100,290)
        self.write(self.rs,False,"center",("Courier",60,"bold"))   
    def lp(self):
        self.ls+=1
        self.upscore()
    def rp(self):
        self.rs+=1
        self.upscore()