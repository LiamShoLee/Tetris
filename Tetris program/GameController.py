import pygame
import random
from other import *
from check import *
from factory import *
from score import *


class GameController():
    def event_handler(self, screen, current_piece, grid):
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
                    current_piece = self.move_left(current_piece, grid)
                if event.key == pygame.K_RIGHT:
                    current_piece = self.move_right(current_piece, grid)
                if event.key == pygame.K_DOWN:
                    current_piece = self.move_down(current_piece, grid)
                if event.key == pygame.K_UP:
                    current_piece = self.rotate_block(current_piece, grid)
        return current_piece

    def move_left(self, current_piece, grid):
        """Moves the current block to the left by one tile

        Parameters:
            current_piece (Block): data for block object
            grid (2D array): block object containing all information regarding the block

        Returns:
            current_piece (Block): data for block object
        """
        current_piece.deviation_x(-1)
        if not(valid_space(current_piece, grid)):
            current_piece.deviation_x(1)
        return current_piece
    
    def move_right(self, current_piece, grid):
        """Moves the current block to the right by one tile

        Parameters:
            current_piece (Block): data for block object
            grid (2D array): block object containing all information regarding the block

        Returns:
            current_piece (Block): data for block object
        """
        current_piece.deviation_x(1)
        if not(valid_space(current_piece, grid)):
            current_piece.deviation_x(-1)
        return current_piece
    
    def move_down(self, current_piece, grid):
        """Moves the current block to the down by one tile

        Parameters:
            current_piece (Block): data for block object
            grid (2D array): block object containing all information regarding the block

        Returns:
            current_piece (Block): data for block object
        """
        current_piece.deviation_y(1)
        if not(valid_space(current_piece, grid)):
            current_piece.deviation_y(-1)
        return current_piece
    
    def rotate_block(self, current_piece, grid):
        """Rotate the current block clockwise by 90 degrees

        Parameters:
            current_piece (Block): data for block object
            grid (2D array): block object containing all information regarding the block

        Returns:
            current_piece (Block): data for block object
        """
        current_piece.rotate_shape(1)
        if not(valid_space(current_piece, grid)):
            current_piece.rotate_shape(-1)
        return current_piece