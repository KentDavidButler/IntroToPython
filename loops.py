#thinking of types of game loops

is_game_over = False
p_x_pos = 0
e_x_pos = 3
end_x_pos = 10

while not is_game_over:
    #do something while the game is not over
    print('Player Pos: {}'.format(p_x_pos))
    print('Enemy Pos: {}'.format(e_x_pos))
    if p_x_pos == e_x_pos:
        print('You Lose')
        is_game_over = True
    elif p_x_pos >= end_x_pos:
        print('You Win')
        is_game_over = True
    else:
        p_x_pos += 2
        e_x_pos += 1

x_pos = 5
movements = [1, -2, 6, -3, -2, 4]

#for 'temp variable' in 'tuple or list'
#always visits every element in array
for movement in movements:
    x_pos += movement
print(x_pos)

