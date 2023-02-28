from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.n=0
        with open("./data.txt") as f:
            self.s=int(f.read())
        self.dis()
    def track(self):
        """Add score"""
        self.n+=1
    def reset(self):
        if self.n>self.s:
            self.s=self.n
            with open("./data.txt","w") as f:
                f.write(str(self.s))
        self.n=0
        self.dis()
    # def gv(self):
    #     """Shows that the game is over"""
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER",move=False,align="center",font=("Courier",20,"bold"))
    def dis(self):
        """Display the scores"""
        self.clear()
        self.hideturtle()
        self.goto(0,280)
        self.color("white")
        self.write(arg=f"SCORE: {self.n}  High Score: {self.s}",move=False,align="center",font=("Courier",15,"bold"))
