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
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    win.blit(label, (top_left_x + p_width /2 - (label.get_width()/2), top_left_y + p_height/2 - label.get_height()/2))


def draw_grid(win, grid):
    """Draws the grid of the playable area for tetris

    Parameters:
        win: window to print on
        grid: the grid that is needed to be printed

    Output: renders the specified grid on the window
    """
    tlx = top_left_x
    tly = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(win, (128,128,128), (tlx, tly + i*block_size), (tlx+p_width, tly+ i*block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(win, (128, 128, 128), (tlx + j*block_size, tly),(tlx + j*block_size, tly + p_height))
            
def draw_next_shape(shape, win):
    """Generates and renders the next shape that will drop in the tetris game
    
    Parameters: 
        shape: the shape that will be generated next
        win: the window to print on

    Output: Generates and renders the next shape in a little square in the top right corner of the application window
    """

    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255))

    tlx = top_left_x + p_width + 50
    tly = top_left_y + p_height/2 - 100
    format = shape.get_shape()[shape.get_rotation() % len(shape.get_shape())]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(win, shape.get_color(), (tlx + j*block_size, tly + i*block_size, block_size, block_size), 0)

    win.blit(label, (tlx + 10, tly - 30))


def draw_window(win, grid, score=0, lines_eliminated = 0, game_level=1, play_mode="Player", game_mode="Normal"):
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

    win.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris Group 19', 1, (255, 255, 255))
    win.blit(label, (top_left_x + p_width / 2 - (label.get_width() / 2), 30))

    font = pygame.font.SysFont('comicsans', 30)
    
    #Display current score
    label = font.render('Score: ' + str(score), 1, (255,255,255))
    tlx = top_left_x + p_width + 50
    tly = top_left_y + p_height/2 - 100
    win.blit(label, (tlx + 20, tly + 160))

    #Display number of lines eliminated
    label = font.render('Lines removed: ' + str(lines_eliminated), 1, (255, 255, 255))
    win.blit(label, (tlx + 10, tly - 120))

    #Display game level
    label = font.render('Level: ' + str(game_level), 1, (255, 255, 255))
    win.blit(label, (tlx + 10, tly - 160))
    
    #Display play mode
    label = font.render('Play Mode: ' + play_mode, 1, (255, 255, 255))
    win.blit(label, (tlx - 650, tly - 140))

    #Display game mode
    label = font.render('Game Mode: ' + game_mode, 1, (255, 255, 255))
    win.blit(label, (tlx - 650, tly - 100))
      
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(win, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)

    pygame.draw.rect(win, (255, 0, 0), (top_left_x, top_left_y, p_width, p_height), 5)

    draw_grid(win, grid)