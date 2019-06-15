#Basic game setup and set up the display
#we will create some functionality that pygame already has
import pygame


#initial pygame
pygame.init()
#setting up basic screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'GAME TIME NOW'
# Colors according to RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
#setting up clock and how often it updates per sec
clock = pygame.time.Clock()
TICK_RATE = 60
is_game_over = False

game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_screen.fill(WHITE_COLOR)
pygame.display.set_caption(SCREEN_TITLE)

#game loop: something that contains all of the game logic
while not is_game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True

        print(event)

    #needed logic to update the screen and graphics
    pygame.display.update()
    #tick the clock to update everything within the game
    clock.tick(TICK_RATE)

#when loop is ever we quit pygame and quit console
pygame.quit()
quit()

