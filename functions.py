#Basics of functions in Python
x_pos = 0
e_x_pos = 4

def move_by(amount):
    global x_pos
    x_pos += amount

move_by(5)

move_by(2)
print(x_pos)

def check_for_collision():
    global x_pos
    global e_x_pos
    if x_pos == e_x_pos:
        return True
    else:
        return False
 
did_collide = check_for_collision()

print(x_pos)
print(did_collide)
