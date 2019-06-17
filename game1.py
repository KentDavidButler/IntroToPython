#Basic game setup and set up the display
#we will create some functionality that pygame already has
import pygame
import sys, os

#setting up basic screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'GAME TIME NOW'
# Colors according to RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()

class Game:
    TICK_RATE = 60
    
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)
    
    def run_game_loop(self):
        is_game_over = False

        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                print(event)
            pygame.display.update()
            clock.tick(self.TICK_RATE)

pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

pygame.quit()
quit()