import pygame
from pygame import mixer
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

    change_block = False
    run = True
    current_block = BlockFactory().create_block(random.randrange(9))
    next_block = BlockFactory().create_block(random.randrange(9))
    clock = pygame.time.Clock()
    difficulty_timer = 0
    fall_timer = 0
    fall_speed = 0.27

    score = 0
    block_controller = GameController()
    mixer.init()
    mixer.music.load('song.wav')
    mixer.music.set_volume(0.2)
    mixer.music.play()
    while run:
        grid = create_grid(locked_positions)
        fall_timer += clock.get_rawtime()
        difficulty_timer += clock.get_rawtime()
        clock.tick()

        if difficulty_timer/1000 > 5:
            difficulty_timer = 0
            if difficulty_timer > 0.12:
                fall_speed -= 0.005

        if fall_timer/1000 > fall_speed:
            fall_timer = 0
            current_block.deviation_y(1)
            if not(valid_space(current_block, grid)) and current_block.get_y() > 0:
                current_block.deviation_y(-1)
                change_block = True
        
        current_block = block_controller.event_handler(win,current_block,grid)
        if current_block is None:
            return
                        
        shape_pos = get_shape_position(current_block)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_block.get_color()

        if change_block:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_block.get_color()
            current_block = next_block
            next_block = BlockFactory().create_block(random.randrange(9))
            change_block = False
            score += clear_rows(grid, locked_positions)

        draw_window(win, grid, score)
        draw_next_shape(next_block, win)
        pygame.display.update()

        if check_lost(locked_positions):
            draw_message(win, "GAME OVER!", 85, (255,255,255))
            pygame.display.update()
            pygame.time.delay(2000)
            run = False
            #top score functionality here
    pygame.display.quit
    mixer.music.stop()