import sys
import pygame

pygame.init()

clock = pygame.time.Clock()

screen_width = 1070
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Name of Game")

font = pygame.font.Sysfont("comicsansms", 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    clock.tick(15)