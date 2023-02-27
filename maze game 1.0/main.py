#Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def up_down():
    turn_left()
    n=0
    while not right_is_clear():
        move()
        n+=1
    turn_right()
    move()
    turn_right()
    for i in range(n):
        move()
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        if front_is_clear():
            move()
    elif front_is_clear() and wall_on_right():
        turn_left()
        if front_is_clear():
            move()
    elif not (front_is_clear() and right_is_clear()):
        turn_left()
        if front_is_clear():
            move()
#OR
# #My final
def turn_right():
    turn_left()
    turn_left()
    turn_left()           
while not at_goal():
    if wall_on_right() and front_is_clear():
            move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
        if front_is_clear():
            move()
#Correction
def turn_right():
    turn_left()
    turn_left()
    turn_left()           
while not at_goal():
    while front_is_clear():
        move()
    if wall_on_right() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
        if front_is_clear():
            move()        