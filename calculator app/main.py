#While loops,Flag and Recursion
from art import logo
#Add
def add(n1,n2):
    """"Add n2 to n1"""
    return n1+n2
#Substract
def sub(n1,n2):
    """"Substracts n2 from n1"""
    return n1-n2
#Multiply
def mul(n1,n2):
    """Multiplies n1 by n2"""
    return n1*n2
#Divide
def div(n1,n2):
    """Divide n1 by n2"""
    return n1/n2
operate={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculate():
    print(logo)
    num1=float(input("What is the first number?: "))
    for i in operate:
        print(i)
    o=input("Enter operation to perform?: ")
    num2=float(input("What is the second number?: "))
    func=operate[o]
    ans=round(func(num1,num2),2)
    print(f"{num1} {o} {num2} = {ans}")
    aa=input(f"Type 'y' to continue calculating with {ans}, or type 'n to exit.: ")
    while aa=="y":
        o=input("Enter operation to perform?: ")
        num3=float(input("What is the next number?: "))
        func=operate[o]
        ans1=round(func(ans,num3),2)
        print(f"{ans} {o} {num3} = {ans1}")
        ans=ans1
        aa=input(f"Type 'y' to continue calculating with {ans}, or type 'n to start a new calculation: ")
    if aa=="n":
        print("You are are done with your calculation")
        #Recursion
        calculate()
calculate()