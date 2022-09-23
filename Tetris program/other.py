import pygame
import button
import sys

def create_grid(locked_pos={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j,i)]
                grid[i][j] = c
    return grid

def quit_game(screen):
    
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
            return True
        if no_button.button_poller():
            quit = False
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pass
        pygame.display.update()