import pygame
from factory import *
from score import *
from draw import *
from check import *
from other import *
from GameController import GameController
import random

pygame.font.init()

def main(win):
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = BlockFactory().create_block(random.randrange(9))
    next_piece = BlockFactory().create_block(random.randrange(9))
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0
    block_controller = GameController()
    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time/1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005

        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_piece.deviation_y(1)
            if not(valid_space(current_piece, grid)) and current_piece.get_y() > 0:
                current_piece.deviation_y(-1)
                change_piece = True
        
        current_piece = block_controller.event_handler(win,current_piece,grid)
        if current_piece is None:
            return
                        
        shape_pos = get_shape_position(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.get_color()

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.get_color()
            current_piece = next_piece
            next_piece = BlockFactory().create_block(random.randrange(9))
            change_piece = False
            score += clear_rows(grid, locked_positions)

        draw_window(win, grid, score)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            draw_message(win, "GAME OVER!", 80, (255,255,255))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            #top score functionality here
    pygame.display.quit