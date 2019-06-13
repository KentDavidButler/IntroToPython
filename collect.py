#arrays lists and dictionaries
#tuples are non mutable
#arrays/lists are mutable and are the same thing

size = (100,200)
print(size)
print(size[0])

new_size = size + (300,) #single valuse need a comma

#check if a collection contains an element
does_contain = 100 in new_size
print(does_contain)

array/list
movement = [5, -2, -3, 4, -1]
movement[0] = 7 #changing the element at a location
movement.append(-5) #adds to the end, elements don't have to be same type
movement.remove(-3) #removes passed value
len(movement)
max(movement)
min(movement)

#dictionaries
#first variable is the key, the second is the value
starting_positions = {'player_0': 50, 'player_1': 150}
starting_positions.keys() #prints out all keys
