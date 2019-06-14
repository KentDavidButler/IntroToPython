#objects and classes
#naming 
#variables are lower_case_with_underscore
#classes are UpperCaseForFirstLetters

class GameCharacter:
    #constructor class
    
    speed = 5

    def __init__(self, name, width, height, x_pos, y_pos)
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

#using the class
character_0 = GameCharacter('char_0', 50, 100, 100, 100)
print(character_0.name)
print(character_0.x_pos)
character_0.move(50,10)
print(character_0.x_pos)
