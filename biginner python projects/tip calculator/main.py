"""some beginner code in my journey of studying python.
this code aims ata calculating the tip per person among friends in an outing"""

print("--------------------welcome to the tip calculator-----------------\n")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("what percentage tip would you like to give?, 10,12 0r 15: "))
people = int(input("how many people would you like to split the bill"))
bill = total_bill / people
percentage_tip = bill * (percentage / 100)
print(f'each person should pay ${round((bill + percentage_tip), 2)}.')
