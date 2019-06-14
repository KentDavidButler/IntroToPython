#subclass, super class and inheritance

class GameCharacter:

    def __init__(self, name, width, height, x_pos, y_pos)
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

class PlayerCharcter(GameCharacter):
    #user the exisitng constructor from the superclass be sure to delete self in the super.__init__
    def __init__(self, name, width, height, x_pos, y_pos):
        super().__init__( name, width, height, x_pos, y_pos)
    
    def __init__(self, name, x_pos, y_pos):
        super().__init__(name, 100, 100, x_pos, y_pos)
    
    def move(self, by_y_amount):
        super().move(0, by_y_amount)

#to override an existing method, you can define a method and not use the 'super()' and instead you create what ever new logic you need


