from turtle import width
import pygame
import factory

win_width = 1000
win_height = 700
p_width = 300  #30 width per block
p_height = 600  #30 height per block
block_size = 30

top_left_x = (win_width - p_width) // 2
top_left_y = win_height - p_height

def draw_message(win, text, size, color):
    """Renders a message on the display window 

    Parameters: 
        text: what message to render
        size: the size of the font
        color: the color of the message
    
    Output: renders a message with the input variables assigned to its attributes
    
    """
    font = pygame.font.Font("assets/MarioFont/SuperMario256.ttf", size, bold=True)
    label = font.render(text, 1, color)

    win.blit(label, (top_left_x + p_width /2 - (label.get_width()/2), top_left_y + p_height/2 - label.get_height()/2))


def draw_grid(win, grid, field_width, field_height):
    """Draws the grid of the playable area for tetris

    Parameters:
        win: window to print on
        grid: the grid that is needed to be printed

    Output: renders the specified grid on the window
    """
    win_size = pygame.display.get_window_size()
    tlx = win_size[0] // 3 
    tly = win_size[1] // 7
    for i in range(len(grid)):
        pygame.draw.line(win, (128,128,128), (tlx, (tly + i*block_size)), ((tlx + field_width*block_size), tly+ i*block_size))
    for j in range(len(grid[1])):
       pygame.draw.line(win, (128, 128, 128), (tlx + j*block_size, tly),(tlx + j*block_size, tly + field_height*block_size))

            
def draw_next_shape(shape, win, field_width, field_height):
    """Generates and renders the next shape that will drop in the tetris game
    
    Parameters: 
        shape: the shape that will be generated next
        win: the window to print on

    Output: Generates and renders the next shape in a little square in the top right corner of the application window
    """

    font = pygame.font.Font('assets/MarioFont/SuperMario256.ttf', 30)
    label = font.render('Next Shape', 1, (255,255,255))
    win_size = pygame.display.get_window_size()
    tlx = win_size[0] + field_width*block_size + 50
    tly = win_size[1] + field_height*block_size/2 - 100
    format = shape.get_shape()[shape.get_rotation() % len(shape.get_shape())]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(win, shape.get_color(), (tlx + j*block_size, tly + i*block_size, block_size, block_size), 0)

    win.blit(label, (tlx + 10, tly - 30))


def draw_window(win, grid,  field_width, field_height, score=0, lines_eliminated = 0, game_level=1, play_mode=0, game_mode=0):
    """Draws the game window with the attributes of the game displayed

    Parameters: 
        win: the window to print on
        grid: the playable grid
        score: the current score (defaulted to 0)
        gameLevel: the current game level (defaulted to 1)
        play_mode: the play mode (defaulted to "Player")
        game_mode: the game mode (defaulted to "Normal")

    Output: prints all the input information in a window that will be used for the tetris game     
    """
    win_size = pygame.display.get_window_size()
    square_tlx = win_size[0] // 3 
    square_tly = win_size[1] // 7
    win.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.Font('assets/MarioFont/SuperMario256.ttf', 60)
    label = font.render('Tetris Group 19', 1, (255, 255, 255))
    win.blit(label, (((win_size[0] - label.get_width()) / 2), 25))

    font = pygame.font.Font('assets/MarioFont/CHLORINP.ttf', 25)
    
    #Display current score
    label = font.render('Score: ' + str(score), 1, (255,255,255))
    tlx = square_tlx + field_width*block_size + 50
    tly = square_tly + field_height*block_size/2 - 100
    win.blit(label, (tlx + 20, tly + 160))

    #Display number of lines eliminated
    label = font.render('Lines removed: ' + str(lines_eliminated), 1, (255, 255, 255))
    win.blit(label, (tlx + 10, tly - 120))

    #Display game level
    label = font.render('Level: ' + str(game_level), 1, (255, 255, 255))
    win.blit(label, (tlx + 10, tly - 160))
    
    #Display play mode
    if play_mode:
        play_mode = "Extended"
    else :
        play_mode = "Normal"
    label = font.render('Play Mode: ' + play_mode, 1, (255, 255, 255))
    win.blit(label, (square_tlx - label.get_width() - 50, tly - 140))

    #Display game mode
    if game_mode:
        game_mode = "A.i"
    else:
        game_mode = "Player"
    label = font.render('Game Mode: ' + game_mode, 1, (255, 255, 255))
    win.blit(label, (square_tlx - label.get_width() - 50, tly - 100))
      
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(win, grid[i][j], (square_tlx + j*block_size, square_tly + i*block_size, block_size, block_size), 0)



    pygame.draw.rect(win, (255, 0, 0), (square_tlx, square_tly, field_width*30, field_height*30), 5)

    draw_grid(win, grid, field_width, field_height)