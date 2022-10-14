from tkinter import FLAT
from check import *
from factory import *
import pygame
import copy



class TetrisAi:

    def __init__ (self,field_width, field_height):
        self.current_move = 0
        self.next_move = 0
        self.tetris_grid = [[0 for x in range(field_height)] for y in range(field_width)]
        self.bottom_row_positions = [(x,field_height) for x in range(field_width)]
        self.current_block = None
        self.locked_squares = []
        self.bounds = field_width - 1
        self.moves_list = []
        self.ai_delay = 0

    def tetris_ai_loop(self, grid, width, height, current_block, locked_blocks):
    #finds the spot it wants to put the tile
    #possibly use genetic algorythm
        self.update_data(current_block, locked_blocks)
        placement = self.choose_placement(grid, width, height)
        self.navigate_block(placement)
        return 


    def navigate_block(self, placement):
        position = self.current_block.get_x()
        for i in range(placement[1]):
            self.moves_list.append(pygame.event.Event(pygame.KEYDOWN, key = pygame.K_UP))
        delta_x = placement[0] - position
        for x in range(abs(delta_x)):
            if delta_x > 0:
                self.moves_list.append(pygame.event.Event(pygame.KEYDOWN,key =pygame.K_RIGHT)) 
            if delta_x < 0:
                self.moves_list.append(pygame.event.Event(pygame.KEYDOWN,key =pygame.K_LEFT))
        self.moves_list.append(pygame.event.Event(pygame.KEYDOWN,key =pygame.K_SPACE))
        return


    def ai_move(self):
        if self.ai_delay >=40:
            self.ai_delay = 0
            if self.moves_list:
                pygame.event.post(self.moves_list[0])
                self.moves_list.pop(0)
        self.ai_delay += 1
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
        self.locked_squares.extend(self.bottom_row_positions)
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
            clear = True
            for i in range(square[1]-1):
                if ((square[0],square[1]-1-i) in self.locked_squares):
                    clear = False
            if clear:
                field_surface.add((square[0],square[1]-1))
                for i in range(square[1]-1):
                    if (((square[0]-1,square[1]-2-i) in self.locked_squares) or ((square[0]+1,square[1]-2-i) in self.locked_squares)):
                        field_surface.add((square[0],square[1]-2-i))
        field_surface = list(field_surface)
        field_surface.sort(reverse=1,key = lambda square : (square[1], square[0]))
        return field_surface

    def choose_placement(self, grid, width, height):
        ranked_options = self.tetris_grid_surface_scored()
        placement_short_list = []
        pos = (self.current_block.get_x() ,self.current_block.get_y())
        for option in ranked_options:
            for rotation in range(len(self.current_block.shape)):
                self.current_block.rotate_shape(rotation)
                self.current_block.set_pos(option[0],option[1])
                test_shape = get_shape_position(self.current_block)
                flatness = shape_flatness(test_shape)
                if (valid_space(self.current_block,grid,width, height) and option in test_shape):
                    self.current_block.rotate_shape(-rotation)
                    self.current_block.set_pos(pos[0],pos[1])
                    placement_short_list.append((option[0],rotation, option[1], flatness))
                    continue
                self.current_block.set_pos(option[0]-1,option[1])
                test_shape = get_shape_position(self.current_block)
                if (valid_space(self.current_block,grid,width, height) and option in test_shape):
                    self.current_block.rotate_shape(-rotation)
                    self.current_block.set_pos(pos[0],pos[1])
                    placement_short_list.append( (option[0]-1,rotation, option[1], flatness))
                    continue
                self.current_block.set_pos(option[0]-2,option[1])
                test_shape = get_shape_position(self.current_block)
                if (valid_space(self.current_block,grid,width, height) and option in test_shape):
                    self.current_block.rotate_shape(-rotation)
                    self.current_block.set_pos(pos[0],pos[1])
                    placement_short_list.append( (option[0]-2,rotation, option[1], flatness))
                    continue
                self.current_block.set_pos(option[0]-3,option[1])
                test_shape = get_shape_position(self.current_block)
                if (valid_space(self.current_block,grid,width, height) and option in test_shape):
                    self.current_block.rotate_shape(-rotation)
                    self.current_block.set_pos(pos[0],pos[1])
                    placement_short_list.append( (option[0]-3,rotation, option[1], flatness))
                    continue
                self.current_block.set_pos(option[0]+1,option[1])
                test_shape = get_shape_position(self.current_block)
                if (valid_space(self.current_block,grid,width, height) and option in test_shape):
                    self.current_block.rotate_shape(-rotation)
                    self.current_block.set_pos(pos[0],pos[1])
                    placement_short_list.append( (option[0]+1,rotation, option[1], flatness)) 
                    continue
                self.current_block.set_pos(option[0]+2,option[1])
                test_shape = get_shape_position(self.current_block)
                if (valid_space(self.current_block,grid,width, height) and option in test_shape):
                    self.current_block.rotate_shape(-rotation)
                    self.current_block.set_pos(pos[0],pos[1])
                    placement_short_list.append((option[0]+2,rotation, option[1], flatness))
                    continue
                self.current_block.set_pos(option[0]+3,option[1])
                test_shape = get_shape_position(self.current_block)
                if (valid_space(self.current_block,grid,width, height) and option in test_shape):
                    self.current_block.rotate_shape(-rotation)
                    self.current_block.set_pos(pos[0],pos[1])
                    placement_short_list.append((option[0]+3,rotation, option[1], flatness))
                    continue
                self.current_block.rotate_shape(-rotation)
                self.current_block.set_pos(pos[0],pos[1])
            if placement_short_list:
                placement_short_list.sort(reverse =1, key = lambda placement : (placement[3],placement[2],placement[1],placement[0]) )
                for placement in placement_short_list:
                    clear = True
                    self.current_block.rotate_shape(placement[1])
                    for i in range(placement[2]):                            
                        self.current_block.set_pos(placement[0],i+1)
                        if not valid_space(self.current_block,grid,width, height):
                            clear = False
                    self.current_block.rotate_shape(-placement[1])
                    if clear:
                        self.current_block.set_pos(pos[0],pos[1])
                        return placement

        return (width-1, 0)

