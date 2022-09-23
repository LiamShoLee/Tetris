import pygame
import random
from other import quit_game
from check import *
from factory import *
from score import *

s_width = 1000
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 30 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

class View():
    def draw_text_middle(self, surface, text, size, color):
        font = pygame.font.SysFont("comicsans", size, bold=True)
        label = font.render(text, 1, color)

        surface.blit(label, (top_left_x + play_width /2 - (label.get_width()/2), top_left_y + play_height/2 - label.get_height()/2))


    def draw_grid(self, surface, grid):
        sx = top_left_x
        sy = top_left_y

        for i in range(len(grid)):
            pygame.draw.line(surface, (128,128,128), (sx, sy + i*block_size), (sx+play_width, sy+ i*block_size))
            for j in range(len(grid[i])):
                pygame.draw.line(surface, (128, 128, 128), (sx + j*block_size, sy),(sx + j*block_size, sy + play_height))
                
    def draw_next_shape(self, shape, surface):
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Next Shape', 1, (255,255,255))

        sx = top_left_x + play_width + 50
        sy = top_left_y + play_height/2 - 100
        format = shape.get_shape()[shape.get_rotation() % len(shape.get_shape())]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(surface, shape.get_color(), (sx + j*block_size, sy + i*block_size, block_size, block_size), 0)

        surface.blit(label, (sx + 10, sy - 30))


    #When passing through this parameter can someone create a structure so that we don't have to pass through so many parameters?
    def draw_window(self, surface, grid, score=0, lines_eliminated = 0, gameLevel=1, play_mode="Player", game_mode="Normal"):
        surface.fill((0, 0, 0))

        pygame.font.init()
        font = pygame.font.SysFont('comicsans', 60)
        label = font.render('Tetris Group 19', 1, (255, 255, 255))
        surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

        font = pygame.font.SysFont('comicsans', 30)
        #Display current score
        label = font.render('Score: ' + str(score), 1, (255,255,255))
        sx = top_left_x + play_width + 50
        sy = top_left_y + play_height/2 - 100
        surface.blit(label, (sx + 20, sy + 160))

        #Display number of lines eliminated
        label = font.render('Lines removed: ' + str(lines_eliminated), 1, (255, 255, 255))
        surface.blit(label, (sx + 10, sy - 120))

        #Display game level
        label = font.render('Level: ' + str(gameLevel), 1, (255, 255, 255))
        surface.blit(label, (sx + 10, sy - 160))
        
        #Display play mode
        label = font.render('Play Mode: ' + play_mode, 1, (255, 255, 255))
        surface.blit(label, (sx - 650, sy - 140))

        #Display game mode
        label = font.render('Game Mode: ' + game_mode, 1, (255, 255, 255))
        surface.blit(label, (sx - 650, sy - 100))
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)

        pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)

        self.draw_grid(surface, grid)

class Controller():
    def event_handler(self, win, current_piece, grid):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if quit_game(win): return #Nick to change

            if event.type == pygame.KEYDOWN:
                if quit_game(win): return #Nick to change

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
        return current_piece, next_piece
    
    def assign_colors(shape_pos, grid, current_piece):
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.get_color()
        return grid

    def lock_block(shape_pos, locked_positions, current_piece):
        for pos in shape_pos:
            p = (pos[0], pos[1])
            locked_positions[p] = current_piece.get_color()
        return locked_positions
        