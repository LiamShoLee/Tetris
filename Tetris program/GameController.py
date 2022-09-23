import pygame
import random
from other import quit_game
from check import *
from factory import *
from score import *


class GameController():
    def event_handler(self, screen, current_piece, grid):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if quit_game(screen): return #Nick to change

            if event.type == pygame.KEYDOWN:
                if quit_game(screen): return #Nick to change

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
        current_piece.deviation_x(-1)
        if not(valid_space(current_piece, grid)):
            current_piece.deviation_x(1)
        return current_piece
    
    def move_right(self, current_piece, grid):
        current_piece.deviation_x(1)
        if not(valid_space(current_piece, grid)):
            current_piece.deviation_x(-1)
        return current_piece
    
    def move_down(self, current_piece, grid):
        current_piece.deviation_y(1)
        if not(valid_space(current_piece, grid)):
            current_piece.deviation_y(-1)
        return current_piece
    
    def rotate_block(self, current_piece, grid):
        current_piece.rotate_shape(1)
        if not(valid_space(current_piece, grid)):
            current_piece.rotate_shape(-1)
        return current_piece
    
    def create_next_block(current_piece, next_piece):
        current_piece = next_piece
        next_piece = BlockFactory().create_block(random.randrange(9))
    
    def assign_colors(shape_pos, grid, current_piece):
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.get_color()

    def lock_block(shape_pos, locked_positions, current_piece):
        for pos in shape_pos:
            p = (pos[0], pos[1])
            locked_positions[p] = current_piece.get_color()
        