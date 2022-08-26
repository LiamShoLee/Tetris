import enum
import graphlib
from operator import truediv
import pygame
import random


# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - drawWindow
# - rotating shape in main
# - setting up the main

pygame.font.init()

#global variables

##ASSETS

screenWidth = 800             #width of screen
screenHeight = 700            #height of screen
blockSize = 30                #size of block 
boardWidthBlocks = 10
boardHeightBlocks = 20
boardWidth = blockSize*boardWidthBlocks     #includes only playable area
boardHeight = blockSize*boardHeightBlocks    #includes only playable area
top_left_x = (screenWidth - boardWidth) // 2
top_left_y = screenHeight - boardHeight


##SHAPE FORMATS
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colours = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape

##ASSETS
##GAME END CONDITIONS
class Piece(object):
      rows = 20                                             # y coordinate
      columns = 10                                          # x coordinate
      def __init__(self, column, row, shape):
            self.x = column                                 # location column
            self.y = row                                    # location row
            self.shape = shape                              # choose a shape
            self.colour = shape_colours[shapes.index(shape)]  # choose a colour 
            self.rotation = 0                               # number from 0-3 for rotations

def create_grid(locked_positions={}):                             # creates a list of colours (change parameters when editing in menus) 
      grid = [[(0,0,0) for x in range(10)] for x in range(20)]    # create list for every row in grid (each row has 10 blocks with colours in it)
      
      #checks for blocks that have already been dropped and locked
      for i in range(len(grid)):                                  # for rows
            for j in range(len(grid[i])):                         # for columns
                  if (j,i) in locked_positions:                   # if key exists
                        c = locked_positions[(j,i)]               # changes key to
                        grid[i][j] = c                            # changes grid to c
      return grid

def generateShape():
      global shapes, shape_colours                     # call global variables from before (the shapes and colours) 
      return Piece(5, 0, random.choice(shapes))       # generate a random shape in middle top of screen


def draw_grid(surface, grid):                         # draws grid lines
      sx = top_left_x
      sy = top_left_y

      # draws grid lines spaced by blockSize (which may change) for size of board
      for i in range(len(grid)):          # for vertical lines
            pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * blockSize) , (sx + boardWidth, sy + i*blockSize))
            
            for j in range(len(grid[i])):    # for horizontal lines
                  pygame.draw.line(surface, (128, 128, 128), (sx + j*blockSize, sy) , (sx + j * blockSize, sy + boardHeight))
      
      
def drawWindow(surface, grid):                       # draws playable window (which includes title and grid)
      surface.fill((0,0,0))                           # fills grid with black
      # Set up Tetris Title
      pygame.font.init()
      font = pygame.font.SysFont('comicsans', 40)     # change font to super mario 256
      label = font.render('TETRIS Group 19', 1, (255,255,255)) # anti aliasing 1, White Title
      surface.blit(label, (top_left_x + boardWidth/2 - (label.get_width()/2), 30)) # finds middle of screen and puts title in middle
      for i in range(len(grid)):                            
            for j in range(len(grid[i])):
                  pygame.draw.rect(surface, grid[i][j], (top_left_x + j* blockSize, top_left_y + i * blockSize, blockSize, blockSize), 0) 
                  # fills board with blocks
      # draw board border 
      pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, boardWidth, boardHeight), 5)    # makes the boarder around the playable area

      draw_grid(surface,grid)

def convertShapeFormat(shape): # rotates shape
      positions = []
      format = shape.shape[shape.rotation % len(shape.shape)] # chooses the shape rotation based on the value of the shape rotation and possible shapes
      # modulus so it wraps around between 0-3 for most shapes excluding I block

      for i, line in enumerate(format):
            row = list(line)
            for j,column in enumerate(row):
                  if column == '0':       # if the block is in that position
                        positions.append((shape.x + j, shape.y + i)) # adds that position into the list for that coordinate
      for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4) 
            # offset of 2 and 4 exist for horizontal and vertical because without offset, blocks move to the top left (-4 for off top of screen) 
      return positions

def validSpaceChecker(shape, grid): # checks if shape in valid space
      # takes all positions in list and adds it to one dimensional list
      acceptedPosition = [[(j,i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)] # only adds if space is empty (0,0,0)
      acceptedPosition = [j for sub in acceptedPosition for j in sub]
      
      formattedShape = convertShapeFormat(shape)

      for pos in formattedShape: 
            if pos not in acceptedPosition:
                  if pos[1] > -1:   # checks if 
                        return False
      return True


def checkLost(positions):
      # checks if any positions are above screen (TOPPED OUT)
      for pos in positions:
            x, y = pos
            if y < 1: # if above board
                  return True

      return False


def draw_text_middle(text, size, colour, surface):  
    pass

def clearFullRow(grid, locked):
      inc = 0
      for i in range(len(grid)-1,-1,-1):
            row = grid[i]
            if (0,0,0) not in row: # checks for how many rows are deleted
                  inc += 1         # increments for how many rows full 
                  ind = i
                  for j in range(len(row)): # deletes locked positions in the row
                        try:
                              del locked[(j,i)] 
                        except:
                              continue
      
      #shift every above row by 1
      if inc > 0:                                           # if one row is removed
            for key in sorted(list(locked), key = lambda x: x[1])[::-1]: # for every key in the sorted list of locked positions based on y value
                  x, y = key
                  if y < ind:                               # if the row is above the index of the full row, moves all those rows down one
                        newKey = (x, y + inc)               # shifts it down
                        locked[newKey] = locked.pop(key)    # removes from locked positions list


def drawNextShape(shape, surface):
      font = pygame.font.SysFont('comicsans', 30)
      label = font.render('Next Shape', 1, (255, 255, 255))

      sx = top_left_x + boardWidth + 50     # move to right
      sy = top_left_y + boardHeight/2 - 100 # move it higher
      format = shape.shape[shape.rotation % len(shape.shape)]

      for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                  if column == '0':
                        pygame.draw.rect(surface, shape.colour, (sx + j*blockSize, sy + i*blockSize, blockSize,blockSize), 0)
                        # draws rectangle window for exxtra shape

      surface.blit(label, (sx +10, sy - 30)) # draws the stuff


def main(win):
      locked_positions = {}
      grid = create_grid(locked_positions)

      changePiece = False                             
      run = True                                      # game initialised to run
      currentPiece = generateShape()                      # current piece
      nextPiece = generateShape()                         # next piece
      clock = pygame.time.Clock()                     # clock
      fallTime = 0
      fallSpeed = 0.27

      while run:                                      # keeps game running
            grid = create_grid(locked_positions)      # updates grid
            fallTime += clock.get_rawtime()           # keeps track of time by adding time between while loops
            clock.tick() 

            if fallTime/1000 > fallSpeed:
                  fallTime = 0
                  currentPiece.y += 1                                               # moves it down
                  if not (validSpaceChecker(currentPiece, grid)) and currentPiece.y > 0:  # when hits another piece or bottom of screen
                        currentPiece.y -= 1                                         # moves back 
                        changePiece = True                                          # locks piece

            for event in pygame.event.get():          
                  if event.type == pygame.QUIT:             # if condition for game end
                        run = False

                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:      # if left key pressed
                              currentPiece.x -= 1           # move to left
                              if not(validSpaceChecker(currentPiece, grid)): 
                                    currentPiece.x += 1     # checked if invalid and resets

                        if event.key == pygame.K_RIGHT:     # if right key pressed
                              currentPiece.x += 1           # move to right
                              if not(validSpaceChecker(currentPiece, grid)):
                                    currentPiece.x -= 1     # checked if invalid and resets

                        if event.key == pygame.K_DOWN:      # if down key pressed
                              currentPiece.y += 1           # move down one block ################################
                              if not(validSpaceChecker(currentPiece, grid)):
                                    currentPiece.x -= 1     # checked if invalid and resets

                        if event.key == pygame.K_UP:        # if up key pressed
                              currentPiece.rotation += 1    # rotate once
                              if not(validSpaceChecker(currentPiece, grid)):
                                    currentPiece.rotation -= 1    # checked if invalid and resets

            shapePosition = convertShapeFormat(currentPiece)
            for i in range(len(shapePosition)):       # draws current piece
                  x, y = shapePosition[i]
                  if y > -1:                          # position above the board
                        grid[y][x] = currentPiece.colour

            if changePiece:
                  for pos in shapePosition:
                        p = (pos[0], pos[1])
                        locked_positions[p] = currentPiece.colour     #adds current piece to locked positions so it can update at start of while loop
                  currentPiece = nextPiece
                  nextPiece = generateShape()
                  changePiece = False
                  # clear rows only after piece stops moving
                  clearFullRow(grid, locked_positions)
            
            
            drawWindow(win, grid)
            drawNextShape(nextPiece, win)      
            pygame.display.update()
            if checkLost(locked_positions):    # stops game if lost
                  run = False

      pygame.display.quit # quits display 

def main_menu(win): #default window
    main(win)

win = pygame.display.set_mode((screenWidth,screenHeight))   #replace this with the other code you guys have 
pygame.display.set_caption('Tetris')                        #default title screen
main_menu(win)  # start game