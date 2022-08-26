import sys
import pygame
import button

pygame.init()

clock = pygame.time.Clock()

screen_width = 1070
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

#font = pygame.font.Sysfont("comicsansms", 30)

#Load in some buttons
play_img = pygame.image.load('Play_img.png')
exit_img = pygame.image.load('Exit_img.png')
config_img = pygame.image.load('Configure_img.png')

play_button = button.Button(0, 670, play_img, 1)
exit_button = button.Button(970, 670, exit_img, 1)
config_button = button.Button(100, 670, config_img, 1)

playGame = True
while playGame:

    screen.fill((195,195,195))
    if play_button.draw(screen):
        print("start game")
    if exit_button.draw(screen):
        playGame=False
    if config_button.draw(screen):
        print("Configure")
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    clock.tick(15)