import pygame
import random
from other import *
from check import *
from factory import *
from score import *


class GameController():
    def event_handler(self, screen, current_block, grid):
        """Checks for inputs from the player/user and takes appropriate action for each event

        Parameters:
            self: to modify the current game. such as the position of the current movable block
            current_piece: to modify attributes of the current piece such as position or rotation
            grid: to check if the movement is valid and see the current grid

        Returns: 
            current_piece(Block): data for the block object
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if quit_game(screen): return 

                if event.key == pygame.K_LEFT:
                    current_block = self.move_left(current_block, grid)
                if event.key == pygame.K_RIGHT:
                    current_block = self.move_right(current_block, grid)
                if event.key == pygame.K_DOWN:
                    current_block = self.move_down(current_block, grid)
                if event.key == pygame.K_UP:
                    current_block = self.rotate_block(current_block, grid)
                if event.key == pygame.K_p:
                    pause_game(screen)
                if event.key == pygame.K_m:
                    pygame.mixer.music.pause()
                if event.key == pygame.K_u:
                    pygame.mixer.music.unpause()
        return current_block

    def move_left(self, current_block, grid):
        """Moves the current block to the left by one tile

        Parameters:
            current_block (Block): data for block object
            grid (2D array): block object containing all information regarding the block

        Returns:
            current_block (Block): data for block object
        """
        current_block.deviation_x(-1)
        if not(valid_space(current_block, grid)):
            current_block.deviation_x(1)
        return current_block
    
    def move_right(self, current_block, grid):
        """Moves the current block to the right by one tile

        Parameters:
            current_block (Block): data for block object
            grid (2D array): block object containing all information regarding the block

        Returns:
            current_block (Block): data for block object
        """
        current_block.deviation_x(1)
        if not(valid_space(current_block, grid)):
            current_block.deviation_x(-1)
        return current_block
    
    def move_down(self, current_block, grid):
        """Moves the current block to the down by one tile

        Parameters:
            current_block (Block): data for block object
            grid (2D array): block object containing all information regarding the block

        Returns:
            current_block (Block): data for block object
        """
        current_block.deviation_y(1)
        if not(valid_space(current_block, grid)):
            current_block.deviation_y(-1)
        return current_block
    
    def rotate_block(self, current_block, grid):
        """Rotate the current block clockwise by 90 degrees

        Parameters:
            current_block (Block): data for block object
            grid (2D array): block object containing all information regarding the block

        Returns:
            current_block (Block): data for block object
        """
        current_block.rotate_shape(1)
        if not(valid_space(current_block, grid)):
            current_block.rotate_shape(-1)
        return current_block