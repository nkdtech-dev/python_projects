#Number Guessing Game
from random import randint
from art import logo
from replit import clear
def analysis():
    """Provides the random number"""
    return randint(1,100)
def compare(u,m):
    """Compares user input and Machine's choosen number"""
    if u==m:
        print("You guess so well")
        return 0
    elif u>m:
        print("Too High")
        return 1
    else:
        print("Too Low")
        return 2
def action(q):
    """Performs the operation"""
    print(f"You have {q} attempts remaining to guess the number.")
    ans=int(input("Make a guess: "))
    compare(ans,com)
    if compare(ans,com)==0:
        print(f"You got it! The answer was {com}") 
        return 0 
    else:
        if q==0:
            print(f"You've run out of guess! The answer was {com}")
            return 0 
        else:
            print("Guess again")
            q-=1
            action(q)
            return 0
y="yes"
while y=="yes":
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
    ch=input("Choose a difficulty. Type 'easy' or 'hard': ")
    h=5
    e=10
    z=1
    com=analysis()
    while z==1:
        if ch=="hard":
            z=action(h)
        elif ch=="easy":
            z=action(e)
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!Wrong Input!!!!!!!!!!!!!!!!!!!!!!")
            z=0
    y=input("Will you like to play again? 'yes' or 'no': ")
    clear()
print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ HAVE A BLESSED DAY \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")   