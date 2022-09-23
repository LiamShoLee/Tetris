import pygame
import factory

s_width = 1000
s_height = 700
play_width = 300  #30 width per block
play_height = 600  #30 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width /2 - (label.get_width()/2), top_left_y + play_height/2 - label.get_height()/2))


def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, (128,128,128), (sx, sy + i*block_size), (sx+play_width, sy+ i*block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j*block_size, sy),(sx + j*block_size, sy + play_height))
            
def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = shape.get_shape()[shape.get_rotation() % len(shape.get_shape())]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.get_color(), (sx + j*block_size, sy + i*block_size, block_size, block_size), 0)

    surface.blit(label, (sx + 10, sy - 30))


#When passing through this parameter can someone create a structure so that we don't have to pass through so many parameters?
def draw_window(surface, grid, score=0, lines_eliminated = 0, gameLevel=1, play_mode="Player", game_mode="Normal"):
    surface.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris Group 19', 1, (255, 255, 255))
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    font = pygame.font.SysFont('comicsans', 30)
    #Display current score
    label = font.render('Score: ' + str(score), 1, (255,255,255))
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    surface.blit(label, (sx + 20, sy + 160))

    #Display number of lines eliminated
    label = font.render('Lines removed: ' + str(lines_eliminated), 1, (255, 255, 255))
    surface.blit(label, (sx + 10, sy - 120))

    #Display game level
    label = font.render('Level: ' + str(gameLevel), 1, (255, 255, 255))
    surface.blit(label, (sx + 10, sy - 160))
    
    #Display play mode
    label = font.render('Play Mode: ' + play_mode, 1, (255, 255, 255))
    surface.blit(label, (sx - 650, sy - 140))

    #Display game mode
    label = font.render('Game Mode: ' + game_mode, 1, (255, 255, 255))
    surface.blit(label, (sx - 650, sy - 100))
      
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)

    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)

    draw_grid(surface, grid)