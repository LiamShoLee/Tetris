import sys
import pygame
import button
#from topscore import *

pygame.init()

clock = pygame.time.Clock()

screen_width = 1070
screen_height = 720
title_x = (1070-560)/2
title_y = (0)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

font = pygame.font.Font("assets/MarioFont/SuperMario256.ttf", 30)
font2 = pygame.font.Font("assets/MarioFont/SuperMario256.ttf", 32)

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
back_x = exit_x - 100

play_button = button.Button(play_x, (0.95*screen_height-play_img.get_height()*image_scale), play_img, image_scale)
config_button = button.Button(config_x, 0.95*screen_height-config_img.get_height()*image_scale, config_img, image_scale)
score_button = button.Button(score_x, 0.95*screen_height-score_img.get_height()*image_scale, score_img, image_scale)
exit_button = button.Button(exit_x, 0.95*screen_height-exit_img.get_height()*image_scale, exit_img, image_scale)
back_button = button.Button(back_x,0.95*screen_height-back_img.get_height()*image_scale, back_img, image_scale)

topsScoreText = pygame.font.Font.render(pygame.font.Font("assets/MarioFont/SuperMario256.ttf", 48),"Top Scores",True,'black',None)

#configure page texts
configText = pygame.font.Font.render(pygame.font.Font("assets/MarioFont/SuperMario256.ttf", 48),"Configuration",True,('black'),None)
config_x = screen_width*.32
fieldSizeText = pygame.font.Font.render(font2,"Field Size",True,('black'),None)
gameLevelText = pygame.font.Font.render(font2,"Game Level",True,('black'),None)
gameModeText = pygame.font.Font.render(font2,"Game Mode",True,('black'),None)
withExtensionText = pygame.font.Font.render(font2,"Extended Game",True,('black'),None)
extendText = pygame.font.Font.render(font2,"Extended",True,('black'),None)
normalText = pygame.font.Font.render(font2,"Normal",True,('black'),None)
aiText = pygame.font.Font.render(font2,"A.I",True,('black'),None)
playerText = pygame.font.Font.render(font2,"Human",True,('black'),None)
plusText = pygame.font.Font.render(font2,"+",True,('black'),None)
minusText = pygame.font.Font.render(font2,"-",True,('black'),None)

#configure page buttons
fieldSizePlusButton = button.surfaceButton(560,400,plusText)
fieldSizeMinusButton = button.surfaceButton(500,400,minusText)
extendedButton = button.surfaceButton(500,500,extendText)
normalButton = button.surfaceButton(750,500,normalText)
aiButton = button.surfaceButton(500,200,aiText)
playerButton = button.surfaceButton(600,200,playerText)
plusLevelButton = button.surfaceButton(560,300,plusText)
minusLevelButton = button.surfaceButton(500,300,minusText)

#Text for start-up
yearCourseText = pygame.font.Font.render(font2,"2805ICT 2022",True,('black'),None)  #Here
studentText = pygame.font.Font.render(font2,"Adrian Jih -- Liam Lee -- Nick Howe",True,('black'),None)  #Here
def MainMenu():
    RunGame = True
    while RunGame:
        screen.fill((195,195,195))
        screen.blit(title_img,(title_x,title_y))    #Here
        screen.blit(studentText,(150,350))  #Here
        screen.blit(yearCourseText,(100,300)) #Here
        if play_button.draw(screen):
            print("start game")
        if exit_button.draw(screen):
                pygame.quit()
                sys.exit()
        if config_button.draw(screen):
            ConfigMenu()
        if score_button.draw(screen):
            print_score()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): #Here
                print("Esc key pressed")
                
        pygame.display.update()
        clock.tick(15)

def print_score():
    
    scores = [line.strip('\n')
        for line in open('scores.txt', 'r').readlines()]
        
    printScores = True
    while printScores:
        screen.fill((195,195,195))
        if back_button.draw(screen):
            printScores = False
        #if exit_button.draw(screen):
         #   pygame.quit()
          #  sys.exit()

        screen.blit(topsScoreText, (screen_width*.33 , 120))
        for n, line in enumerate(scores):
            lines = line.split()
            for x, word in enumerate(lines):
                text = font.render(word, 1, "black")
                screen.blit(text, (screen_width*.33 + x*x*60, 200+n*30))
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        clock.tick(15)
    return


def ConfigMenu():
    RunGame = True
    while RunGame:
        screen.fill((195,195,195))
      #  if exit_button.draw(screen):
      #      pygame.quit()
      #      sys.exit()
        if back_button.draw(screen):
            return
        screen.blit(gameModeText,(100,200))
        if aiButton.draw(screen):
            print('A.I selected')
        if playerButton.draw(screen):
            print('Human Player')

        screen.blit(fieldSizeText,(100,400))
        if fieldSizeMinusButton.draw(screen):
            print("minus")
        if fieldSizePlusButton.draw(screen):
            print("plus")
        screen.blit(pygame.font.Font.render(font2,"4",True,('black'),None),(525,400))
        screen.blit(gameLevelText,(100,300))
        if minusLevelButton.draw(screen):
            print("a")
        if plusLevelButton.draw(screen):
            print("1")
        screen.blit(pygame.font.Font.render(font2,"6",True,('black'),None),(525,300))
        screen.blit(withExtensionText,(100,500))
        if extendedButton.draw(screen):
            print("Extended")
        if normalButton.draw(screen):
            print("Player")

        screen.blit(configText,(config_x,60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        clock.tick(15)

MainMenu()
