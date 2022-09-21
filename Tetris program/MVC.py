import pygame
from other import quit_game
from check import *

class Controller():
    def event_handler(self, win, current_piece, grid):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if quit_game(win): return

            if event.type == pygame.KEYDOWN:
                if quit_game(win): return

            if event.key == pygame.K_LEFT:
                self.move_left(current_piece, grid)
            if event.key == pygame.K_RIGHT:
                self.move_right(current_piece, grid)
            if event.key == pygame.K_DOWN:
                self.move_down(current_piece, grid)
            if event.key == pygame.K_UP:
                self.rotate_block(current_piece, grid)

    def move_left(self, current_piece, grid):
        current_piece.deviation_x(-1)
        if not(valid_space(current_piece, grid)):
            current_piece.deviation_x(1)
    
    def move_right(self, current_piece, grid):
        current_piece.deviation_x(1)
        if not(valid_space(current_piece, grid)):
            current_piece.deviation_x(-1)
    
    def move_down(self, current_piece, grid):
        current_piece.deviation_y(1)
        if not(valid_space(current_piece, grid)):
            current_piece.deviation_y(-1)
    
    def rotate_block(self, current_piece, grid):
        current_piece.rotate_shape(1)
        if not(valid_space(current_piece, grid)):
            current_piece.rotate_shape(-1)
        