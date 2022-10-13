from check import *
from factory import *
import pygame



class TetrisAi:

    def __init__ (self,field_width, field_height):
        self.current_move = 0
        self.next_move = 0
        self.tetris_grid = [[0 for x in range(field_height)] for y in range(field_width)]
        self.current_block = None
        self.locked_squares = []
        self.bounds = field_width - 1
        self.moves_list = []

    def tetris_ai_loop(self, grid, width, height, current_block, locked_blocks):
    #finds the spot it wants to put the tile
    #possibly use genetic algorythm
        self.update_data(current_block, locked_blocks)
        placement = self.choose_placement(grid, width, height)
        self.navigate_block(placement)
        return 


    def navigate_block(self, placement):
        self.moves_list = []
        position = self.current_block.get_x()
        for i in range(placement[1]):
            self.moves_list.append(pygame.event.Event(pygame.K_DOWN)),
        delta_x = placement[0] - position
        for x in range(abs(delta_x)):
            if delta_x > 0:
                self.moves_list.append(pygame.event.Event(pygame.K_RIGHT)) 
            else:
                self.moves_list.append(pygame.event.Event(pygame.K_LEFT))
        self.moves_list.append(pygame.event.Event(pygame.K_SPACE))


    def ai_move(self):
        if self.moves_list:
            pygame.event.post(self.moves_list[0])
            self.moves_list.pop(0)
        return

    def update_data(self,current_block,locked_blocks):
        """Updates the stored game data to match the locked positions and current block
        
            Parameters: 
                self.tetris_grid: the a.i's map of the field
                current_block: the block in play the a.i will place
                locked_blocks: the current locked positions of blocks in the field
            
            Returns: None  
        """
        self.current_block = current_block
        self.locked_squares = [*locked_blocks]
        self.locked_squares.sort(key = lambda square : (square[1], square[0]) ) #sorts top to bottom, left to right
        for i in range(len(self.tetris_grid)):
            for j in range(len(self.tetris_grid[i])):
                if (i, j) in locked_blocks:
                    self.tetris_grid[i][j] = True
                else :
                    self.tetris_grid[i][j] = False
        return

    def tetris_grid_surface_scored(self):
        #Find the upper layer of locked blocks
        #Sort by highest 
        #
        field_surface = set()
        for square in self.locked_squares:
            if not self.tetris_grid[square[0]][square[1]-1]:
                field_surface.add((square[0],square[1]-1))
                if not self.tetris_grid[square[0]][square[1]-2] and not self.tetris_grid[abs(square[0]-1)][square[1]-2]:
                    field_surface.add((square[0],square[1]-2))
        field_surface = list(field_surface)
        field_surface.sort(reverse=1,key = lambda square : (square[1], square[0]))
        return field_surface

    def choose_placement(self, grid, width, height):
        ranked_options = self.tetris_grid_surface_scored()
        pos = (self.current_block.get_x() ,self.current_block.get_y())
        for option in ranked_options:
            for rotation in range(len(self.current_block.shape)):
                self.current_block.rotate_shape(rotation)
                self.current_block.set_pos(option[0],option[1])
                if valid_space(self.current_block,grid,width, height) and option in get_shape_position(self.current_block):
                    self.current_block.rotate_shape(-rotation)
                    self.current_block.set_pos(pos[0],pos[1])
                    return (option[0],rotation)
                self.current_block.set_pos(option[0]-1,option[1])
                if valid_space(self.current_block,grid,width, height) and option in get_shape_position(self.current_block):
                    self.current_block.rotate_shape(-rotation)
                    self.current_block.set_pos(pos[0],pos[1])
                    return (option[0]-1,rotation)
                self.current_block.set_pos(option[0]-2,option[1])
                if valid_space(self.current_block,grid,width, height) and option in get_shape_position(self.current_block):
                    self.current_block.rotate_shape(-rotation)
                    self.current_block.set_pos(pos[0],pos[1])
                    return (option[0]-2,rotation)
        return (width-1, 0)