import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
s=Screen()
s.setup(width=1360,height=768)
s.bgcolor("black")
s.title("DELEOTECH Poke Game")
s.tracer(0)  
s.listen()
lp=Paddle(-655)
rp=Paddle(655)
b=Ball()
sc=Score()
b.move()
s.onkeypress(rp.moveup,"Up")
s.onkeypress(rp.movedown,"Down")
s.onkeypress(lp.moveup,"w")
s.onkeypress(lp.movedown,"s")
g=1
while g==1:
    time.sleep(b.ms)
    s.update()
    b.move()
    #Detect collision with wall
    if b.ycor()>364 or b.ycor()<-364:
        b.bounwall()
     #Detect collision with paddle
    if (b.distance(lp)<50  and b.xcor()<-630) or (b.distance(rp)<50 and b.xcor()>630):
        b.bounpad()
    #Detect ball passes left paddle
    if b.xcor()<-680:
        b.refresh()
        sc.rp()
    #Detect ball passes right paddle 
    if b.xcor()>680:
        b.refresh()
        sc.lp()
s.exitonclick()