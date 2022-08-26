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
play_img = pygame.image.load('Play_img.png').convert_alpha()
exit_img = pygame.image.load('Exit_img.png').convert_alpha()
config_img = pygame.image.load('Configure_img.png').convert_alpha()

play_button = button.Button(100, 200, play_img, 1)
exit_button = button.Button(450, 200, exit_img, 1)

while True:

    screen.fill((195,195,195))
    play_button.draw
    exit_button.draw
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    clock.tick(15)