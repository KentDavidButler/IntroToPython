#Basic game setup and set up the display
#we will create some functionality that pygame already has
import pygame
import sys, os

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

player_image = pygame.image.load('player.png')
#casting an image on an image and scaling it to 50
player_image = pygame.transform.scale(player_image, (50,50))
rect_loc = 350
cir_loc = 300
speed = 5
rect_right = True
cir_right = False

#game loop: something that contains all of the game logic
while not is_game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True

        print(event)
    #move rect right
    if rect_right:
        rect_loc += speed
    else:
        rect_loc -= speed
    if rect_loc >= 700:
        rect_right = False
    if rect_loc <= 0:
        rect_right = True
        
#drawing basic shapes: polygon, ellipse, arc, line, lines, aaline & aalines
    pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
    pygame.draw.circle(game_screen, BLACK_COLOR, (400,300), 50)

    game_screen.blit(player_image, (rect_loc, 375))

    #needed logic to update the screen and graphics
    pygame.display.update()
    #tick the clock to update everything within the game
    clock.tick(TICK_RATE)

#when loop is ever we quit pygame and quit console
pygame.quit()
quit()

