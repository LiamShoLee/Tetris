import sys
import pygame
import button
from topscore import *

pygame.init()

clock = pygame.time.Clock()

screen_width = 1070
screen_height = 720
title_x = (1070-560)/2
title_y = (0)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

#font = pygame.font.Sysfont("comicsansms", 30)

#Load in some buttons
image_scale = 1
play_img = pygame.image.load('assets/Play_img.png')
exit_img = pygame.image.load('assets/Exit_img.png')
config_img = pygame.image.load('assets/Configure_img.png')
score_img = pygame.image.load('assets/Score_img.png')
title_img = pygame.image.load('assets/Cursed_title.png')
back_img = pygame.image.load('assets/Back_img.png')

play_x = .085*screen_width
config_x = play_x+play_img.get_width()*image_scale+screen_width*.10
score_x = config_x + config_img.get_width()*image_scale+screen_width*.10
exit_x = score_x + score_img.get_width()*image_scale+screen_width*.10
back_x = exit_x - screen_width*.10 - back_img.get_width()*image_scale

play_button = button.Button(play_x, 0.95*screen_height-play_img.get_height()*image_scale, play_img, image_scale)
config_button = button.Button(config_x, 0.95*screen_height-config_img.get_height()*image_scale, config_img, image_scale)
score_button = button.Button(score_x, 0.95*screen_height-score_img.get_height()*image_scale, score_img, image_scale)
exit_button = button.Button(exit_x, 0.95*screen_height-exit_img.get_height()*image_scale, exit_img, image_scale)
back_button = button.Button(back_x,0.95*screen_height-back_img.get_height()*image_scale, back_img, image_scale)

def MainMenu():
    RunGame = True
    while RunGame:
        screen.fill((195,195,195))
        if play_button.draw(screen):
            print("start game")
        if exit_button.draw(screen):
                pygame.quit()
                sys.exit()
        if config_button.draw(screen):
            print("This is config")
        if score_button.draw(screen):
            print_score()

        screen.blit(title_img,(title_x,title_y))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        clock.tick(15)


def print_score():
    
    scores = [line.strip('\n')
        for line in open('scores.txt', 'r').readlines()]
    font = pygame.font.Font("assets/MarioFont/SuperMario256.ttf", 16)
    screen = pygame.display.set_mode(screen)
        
    RunGame = True
    while RunGame:
        screen.fill("white")
        if exit_button.draw(screen):
            pygame.quit()
            sys.exit()
        if back_button.draw(screen):
            return


        for n, line in enumerate(scores):
            text = font.render(line, 1, "black")
            text_rect = text.get_rect()
            text_rect.centerx = screen[0]//2
            text_rect.centery = n*25 + 50
            screen.blit(text, text_rect)
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        clock.tick(15)

MainMenu()
