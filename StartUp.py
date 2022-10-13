import sys
from ButtonCommand import *
import pygame
import button
from settings import GameSettings
import TetrisGame


pygame.init()

clock = pygame.time.Clock()
screen_width = 1070
screen_height = 720
title_x = (1070-560)/2
title_y = (0)
flags = pygame.RESIZABLE | pygame.SCALED
screen = pygame.display.set_mode((screen_width, screen_height),flags)
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
heightText = pygame.font.Font.render(font2,"Height",True,('black'),None)
widthText = pygame.font.Font.render(font2,"Width",True,('black'),None)

#configure buttons
play_button = button.Button("play",play_x, (0.95*screen_height-play_img.get_height()*image_scale), play_img, image_scale)
config_button = button.Button("config_button",config_x, 0.95*screen_height-config_img.get_height()*image_scale, config_img, image_scale)
score_button = button.Button("score_button",score_x, 0.95*screen_height-score_img.get_height()*image_scale, score_img, image_scale)
exit_button = button.Button("exit_button",exit_x, 0.95*screen_height-exit_img.get_height()*image_scale, exit_img, image_scale)
back_button = button.Button("back_button",back_x,0.95*screen_height-back_img.get_height()*image_scale, back_img, image_scale)

field_height_plus_button = button.SurfaceButton("field_height_blus_button",705,400,plusText)
field_height_minus_button = button.SurfaceButton("field_height_minus_button",635,400,minusText)
field_width_plus_button = button.SurfaceButton("field_width_plus_button",965,400,plusText)
field_width_minus_button = button.SurfaceButton("field_width_minus_button",890,400,minusText)
extended_button = button.SurfaceButton("extended_button",500,500,extendText)
normal_button = button.SurfaceButton("normal_button",750,500,normalText)
ai_button = button.SurfaceButton("ai_button",500,200,aiText)
player_button = button.SurfaceButton("player_button",600,200,playerText)
plus_level_button = button.SurfaceButton("plus_level_button",560,300,plusText)
minus_level_button = button.SurfaceButton("minus_level_button",500,300,minusText)

main_menu_buttons = [play_button,config_button,score_button,exit_button]
config_menu_buttons = [field_height_plus_button,field_height_minus_button,field_width_plus_button,field_width_minus_button,
                       extended_button,normal_button,ai_button,player_button,plus_level_button,minus_level_button,back_button]



#Text for start-up
yearCourseText = pygame.font.Font.render(font2,"2805ICT 2022",True,('black'),None)  #Here
studentText = pygame.font.Font.render(font2,"Adrian Jih -- Liam Lee -- Nick Howe",True,('black'),None)  #Here

class TetrisMenus:
    def __init__(self,settings_object):
        self.game_settings = settings_object

    def main_menu(self):
        RunGame = True
        while RunGame:
            screen = pygame.display.set_mode((1070, 720),flags)
            screen.fill((195,195,195))
            screen.blit(title_img,(title_x,title_y))
            screen.blit(studentText,(200,380))  #Here
            screen.blit(yearCourseText,(400,420)) #Here
            for button in main_menu_buttons:
                button.draw(screen)
            polling = True
            while (polling):
                for button in main_menu_buttons:
                    if button.button_poller():
                        command_invoker.execute(button.name)
                        polling = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
                pygame.display.update()

    def start_tetris(self):
        TetrisGame.main(screen,self.game_settings)

    def print_score(self):
        
        scores = [line.strip('\n')
            for line in open('scores.txt', 'r').readlines()]
            
        printScores = True
        while printScores:
            screen.fill((195,195,195))
            back_button.draw(screen)


            screen.blit(topsScoreText, (screen_width*.33 , 120))
            for n, line in enumerate(scores):
                lines = line.split()
                for x, word in enumerate(lines):
                    text = font.render(word, 1, "black")
                    screen.blit(text, (screen_width*.33 + x*x*60, 200+n*30))
            polling = True
            while(polling):       
                if back_button.button_poller():
                    command_invoker.execute(back_button.name)
                    polling = False                
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
                pygame.display.update()
            clock.tick(15)
        return


    def config_menu(self):
        RunGame = True
        while RunGame:

            screen.fill((195,195,195))
            screen.blit(gameModeText,(100,200))
            screen.blit(fieldSizeText,(100,400))
            screen.blit(pygame.font.Font.render(font2, str(self.game_settings.field_height),True,('black'),None),(655,400))
            screen.blit(heightText,(500,400))
            screen.blit(widthText,(750,400))
            screen.blit(pygame.font.Font.render(font2,str(self.game_settings.field_width),True,('black'),None),(915,400))
            screen.blit(gameLevelText,(100,300))
            screen.blit(pygame.font.Font.render(font2,str(self.game_settings.game_start_level),True,('black'),None),(525,300))
            screen.blit(withExtensionText,(100,500))
            screen.blit(configText,(config_x,60))
            if self.game_settings.game_mode:
                pygame.draw.ellipse(screen,('red'), pygame.Rect(485,185,85,50), 0)
            else :
                pygame.draw.ellipse(screen,('red'), pygame.Rect(580,185,160,50), 0)

            if self.game_settings.extended:
                pygame.draw.ellipse(screen,('red'), pygame.Rect(485,485,190,50), 0)
            else :
                pygame.draw.ellipse(screen,('red'), pygame.Rect(735,485,180,50), 0)
                
            for button in config_menu_buttons:
                button.draw(screen)

            polling = True
            while(polling):
                for button in config_menu_buttons:
                    if button.button_poller():
                        command_invoker.execute(button.name)
                        polling = False
                print(self.game_settings.game_mode)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
                pygame.display.update()
            clock.tick(15)

    def exit_menu(self):
                pygame.quit()
                sys.exit()


settings = GameSettings()
game_menu = TetrisMenus(settings)
command_list = [(PlayCommand(game_menu),play_button.name), (ConfigCommand(game_menu),config_button.name),
                    (ScoreCommand(game_menu),score_button.name), (ExitCommand(game_menu),exit_button.name),
                    (BackCommand(game_menu),back_button.name),(FieldHeightPlusCommand(settings),field_height_plus_button.name),
                    (FieldHeightMinusCommand(settings),field_height_minus_button.name),(FieldWidthPlusCommand(settings),field_width_plus_button.name),
                    (FieldWidthMinusCommand(settings),field_width_minus_button.name),(ExtendedCommand(settings),extended_button.name),
                    (NormalCommand(settings),normal_button.name),(AiCommand(settings),ai_button.name),
                    (PlayerCommand(settings),player_button.name),(PlusLevelCommand(settings),plus_level_button.name),
                    (MinusLevelCommand(settings),minus_level_button.name)]    

command_invoker = CommandInvoker()
for item in command_list:
    command_invoker.register_command(item[0],item[1])
game_menu.main_menu()