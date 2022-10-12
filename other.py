import pygame
import button
import sys
from score import check_top_score
from draw import *

def create_grid(width ,height , locked_pos={}):
    """Renders the playable grid for the game
    Parameters: 
        locked_pos: the current locked positions of blocks that have already been placed
    
    Return: 
        grid: the data for the grid (checks for locked positions as well) 
    """
    grid = [[(0,0,0) for x in range(width)] for x in range(height)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j,i)]
                grid[i][j] = c
    return grid

def quit_game(screen, score):
    """Creates smaller window that displays an option to quit the game

    Parameters: 
        screen: the application screen/window that is visible/interactable to the user
    
    Output: 
        renders a smaller quit screen with a yes and no button that can be interacted with to exit the game
    """
    
    font2 = pygame.font.SysFont("comicsans", 32)
    quit_width = screen.get_width()
    quit_height = screen.get_height()
    yesText = pygame.font.Font.render(font2,"Yes",True,('black'),None)
    noText = pygame.font.Font.render(font2,"No",True,('black'),None)
    yes_button = button.SurfaceButton("yes",quit_width/2-100,quit_height/2-quit_height/4+100, yesText)
    no_button = button.SurfaceButton("no",quit_width/2,quit_height/2-quit_height/4+100, noText)
    quitText = pygame.font.Font.render(font2,"Quit Game?",True,('black'),None)
    quit = True
    while quit:
        screen.fill("pink", ((quit_width/2-quit_width/4), (quit_height/2-quit_height/4), quit_width/2, quit_height/2))
        screen.blit(quitText, (quit_width/2-125,quit_height/2-quit_height/4))
        yes_button.draw(screen)
        no_button.draw(screen)
        if yes_button.button_poller():
            pygame.mixer.music.stop()
            check_top_score(score, screen)
            return True
        if no_button.button_poller():
            quit = False
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pass
        pygame.display.update()
        
def pause_game(screen):
    pause = True
    pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
        draw_message(screen, "PAUSED", 85, (255,255,255))
        pygame.display.update()
    pygame.mixer.music.unpause()