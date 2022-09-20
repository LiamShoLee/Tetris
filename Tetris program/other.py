import pygame
import button
import sys

def create_grid(locked_pos={}):  # *
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j,i)]
                grid[i][j] = c
    return grid

def quit_game(win):
    
    #This should be changed later so that it's within a function
    font2 = pygame.font.SysFont("comicsans", 32)
    quit_width = win.get_width()
    quit_height = win.get_height()
    yesText = pygame.font.Font.render(font2,"Yes",True,('black'),None)
    noText = pygame.font.Font.render(font2,"No",True,('black'),None)
    yesButton = button.surfaceButton(quit_width/2-100,quit_height/2-quit_height/4+100, yesText)
    noButton = button.surfaceButton(quit_width/2,quit_height/2-quit_height/4+100, noText)
    quitText = pygame.font.Font.render(font2,"Quit Game?",True,('black'),None)
    
    quit = True
    while quit:
        win.fill("pink", ((quit_width/2-quit_width/4), (quit_height/2-quit_height/4), quit_width/2, quit_height/2))
        win.blit(quitText, (quit_width/2-125,quit_height/2-quit_height/4))
        if yesButton.draw(win):
            return True
        if noButton.draw(win):
            quit = False
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pass
        pygame.display.update()