'''
👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇

Make sure to run the below code only in the following URL or please go through readme file:

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Let's define a function to execute one step of the algorithm
def follow_right_edge():
    # try to turn right first
    if right_is_clear():
        turn_right()
        move()
    # if we can't turn right, try to go straight
    elif front_is_clear():
        move()
    # if we can't go straight, turn left
    else:
        turn_left()

# rare_case scenarios where robot is in the centre of maze where 4 sides are open:
while front_is_clear():
    move()
turn_left()

# main loop
while not at_goal():
    follow_right_edge()
