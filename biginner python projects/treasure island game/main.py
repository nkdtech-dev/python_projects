"""treasure hunt game
designed to be navigated upon to find the hidden project"""

# bitmap
print("-------------------------welcome to treasure island--------------------------\n"
      "your mission is to find the treasure")
road = input("you are at a cross road where do you want to go ? \"left' or \"right\n").lower()
if road == "left":
    lake = input("you are at a lake type \"s to swim or \"b to use a boat\n").lower()
    if lake == "s":
        print("you got eaten by a shark\n======GAME OVER =========")
    elif lake == "b":
        print("you found the treasure")
    else:
        print("invalid option")
elif road == "right":
    door = input("you are faced with two doors \"wooden and \"iron which do you open:\n").lower()
    if door == "wooden":
        print("Game over")
    elif door == "iron":
        print("you found the treasure")
    else:
        print("invalid direction")
"""to be updated """
