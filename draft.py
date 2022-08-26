import pygame
import random
import sys
import button


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

def create_grid(lockedPositions={}):                             # creates a list of colours (change parameters when editing in menus) 
      grid = [[(0,0,0) for x in range(10)] for x in range(20)]    # create list for every row in grid (each row has 10 blocks with colours in it)
      
      #checks for blocks that have already been dropped and locked
      for i in range(len(grid)):                                  # for rows
            for j in range(len(grid[i])):                         # for columns
                  if (j,i) in lockedPositions:                   # if key exists
                        c = lockedPositions[(j,i)]               # changes key to
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
      
# gamemode data will need to be called in this function to read in later prototypes
def drawWindow(surface, grid, score = 0, gameLevel = 1):    # draws playable window (which includes title and grid)
      surface.fill((0,0,0))                                 # fills grid with black
      # Set up Tetris Title
      pygame.font.init()
      font = pygame.font.SysFont('comicsans', 40)           # change font to super mario 256
      label = font.render('TETRIS Group 19', 1, (255,255,255)) # anti aliasing 1, White Title
      surface.blit(label, (top_left_x + boardWidth/2 - (label.get_width()/2), 30)) # finds middle of screen and puts title in middle

      # score text
      font = pygame.font.SysFont('comicsans', 30)
      label = font.render('Score: ' + str(score), 1, (255, 255, 255))
      sx = top_left_x + boardWidth + 50     # move to right
      sy = top_left_y + boardHeight/2 - 100 # move it abit higher
      surface.blit(label, (sx + 10, sy - 200))

      # lines removed so far
      font = pygame.font.SysFont('comicsans', 20)
      label = font.render('Lines removed: ' + str(score//10), 1, (255, 255, 255))
      sx = top_left_x + boardWidth + 50     # move to right
      sy = top_left_y + boardHeight/2 - 100 # move it abit higher
      surface.blit(label, (sx + 10, sy - 120))

      # score text
      font = pygame.font.SysFont('comicsans', 20)
      label = font.render('Level: ' + str(gameLevel), 1, (255, 255, 255))
      sx = top_left_x + boardWidth + 50     # move to right
      sy = top_left_y + boardHeight/2 - 100 # move it abit higher
      surface.blit(label, (sx + 10, sy - 160))
      
      # player or ai mode
      font = pygame.font.SysFont('comicsans', 20)
      label = font.render('Mode: Player' , 1, (255, 255, 255))
      sx = top_left_x + boardWidth + 50     # move to right
      sy = top_left_y + boardHeight/2 - 100 # move it abit higher
      surface.blit(label, (sx - 560, sy - 140))
      
      # extended or normal game
      font = pygame.font.SysFont('comicsans', 20)
      label = font.render('Game Mode: Normal' , 1, (255, 255, 255))
      sx = top_left_x + boardWidth + 50     # move to right
      sy = top_left_y + boardHeight/2 - 100 # move it abit higher
      surface.blit(label, (sx - 560, sy - 100))


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

      return inc


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
                        pygame.draw.rect(surface, shape.colour, (sx + j*blockSize, sy + i*blockSize + 10, blockSize,blockSize), 0)
                        # draws rectangle window for exxtra shape

      surface.blit(label, (sx +10, sy - 30)) # draws the stuff


def main(win):
      lockedPositions = {}
      grid = create_grid(lockedPositions)

      changePiece = False                             
      run = True                                      # game initialised to run
      currentPiece = generateShape()                      # current piece
      nextPiece = generateShape()                         # next piece
      clock = pygame.time.Clock()                     # clock
      fallTime = 0
      fallSpeed = 0.27
      levelTime = 0
      gameLevel = 1
      score = 0

      font2 = pygame.font.Font("assets/MarioFont/SuperMario256.ttf", 32)
      quit_width = win.get_width()
      quit_height = win.get_height()
      yesText = pygame.font.Font.render(font2,"Yes",True,('black'),None)
      noText = pygame.font.Font.render(font2,"No",True,('black'),None)
      yesButton = button.surfaceButton(quit_width/2-100,quit_height/2-quit_height/4+100, yesText)
      noButton = button.surfaceButton(quit_width/2,quit_height/2-quit_height/4+100, noText)
      quitText = pygame.font.Font.render(font2,"Quit Game?",True,('black'),None)
      
      while run:                                      # keeps game running
            grid = create_grid(lockedPositions)      # updates grid
            fallTime += clock.get_rawtime()           # keeps track of time by adding time between while loops
            levelTime += clock.get_rawtime()
            clock.tick() 

            if levelTime/1000 > 8: # every 8 seconds increase level and difficulty
                  levelTime = 0
                  gameLevel += 1
                  if fallSpeed > 0.12:
                        fallSpeed -= 0.005

            if fallTime/1000 > fallSpeed:
                  fallTime = 0
                  currentPiece.y += 1                                               # moves it down
                  if not (validSpaceChecker(currentPiece, grid)) and currentPiece.y > 0:  # when hits another piece or bottom of screen
                        currentPiece.y -= 1                                         # moves back 
                        changePiece = True                                          # locks piece

            for event in pygame.event.get():          
                  if event.type == pygame.QUIT:             # if condition for game end
                        pygame.quit()
                        sys.exit()            

                  if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        quitGame = True
                        while quitGame:
                              win.fill("pink", ((quit_width/2-quit_width/4), (quit_height/2-quit_height/4), quit_width/2, quit_height/2))
                              win.blit(quitText, (quit_width/2-125,quit_height/2-quit_height/4))
                              if yesButton.draw(win):
                                    return
                              if noButton.draw(win):
                                    quitGame = False
                              for events in pygame.event.get():
                                    if events.type == pygame.QUIT:
                                          pygame.quit()
                                          sys.exit()
                              pygame.display.update()
                              
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
                        lockedPositions[p] = currentPiece.colour     #adds current piece to locked positions so it can update at start of while loop
                  currentPiece = nextPiece
                  nextPiece = generateShape()
                  changePiece = False
                  
                  score += clearFullRow(grid,lockedPositions) * 10 
            
                  # clear rows only after piece stops moving
                  clearFullRow(grid, lockedPositions)
            
            
            drawWindow(win, grid, score, gameLevel) # game mode data will need to be added here for later prototypes
            drawNextShape(nextPiece, win)      
            pygame.display.update()
            if checkLost(lockedPositions):    # stops game if lost
                  run = False

      pygame.display.quit # quits display 