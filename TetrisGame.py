import pygame
from pygame import mixer
from factory import *
from score import *
from draw import *
from check import *
from other import *
from settings import *
from GameController import GameController
import random
from tetris_ai import TetrisAi



pygame.font.init()

def main(win,game_settings):
    if game_settings.extended:
        rand_range = 9
    else:
        rand_range = 7
    level = game_settings.game_start_level
    if game_settings.game_mode:
        game_ai = TetrisAi(game_settings.field_width, game_settings.field_height)

    flags = pygame.RESIZABLE 
    screen_width = 1070 + (game_settings.field_width-10)*30*(game_settings.field_width>=10)
    screen_height = 720 + (game_settings.field_height-20)*30*(game_settings.field_height>=20)
    win = pygame.display.set_mode((screen_width , screen_height ),flags)
    locked_positions = {}
    change_block = False
    run = True
    grid = create_grid(game_settings.field_width, game_settings.field_height, locked_positions)
    current_block = BlockFactory().create_block(random.randrange(rand_range))
    current_block.set_pos(game_settings.field_width//2 -2 , 1)
    if game_settings.game_mode:
        game_ai.tetris_ai_loop(grid=grid,width = game_settings.field_width, height = game_settings.field_height, current_block = current_block, locked_blocks= {}) 
    next_block = BlockFactory().create_block(random.randrange(rand_range))
    clock = pygame.time.Clock()
    difficulty_timer = 0
    fall_speed = 50000
    fall_timer = 0
    max_speed = 4000
    for x in range(game_settings.game_start_level):
        fall_speed -= (fall_speed - max_speed) * 0.05

    score = 0
    block_controller = GameController(game_settings.field_width,game_settings.field_height)
    mixer.init()
    mixer.music.load('song.wav')
    mixer.music.set_volume(0.01)
    mixer.music.play(9999)
    while run:
        grid = create_grid(game_settings.field_width, game_settings.field_height, locked_positions)
        fall_timer += clock.get_rawtime()
        difficulty_timer += clock.get_rawtime()
        clock.tick_busy_loop(220)

        if  difficulty_timer > 10000:
            difficulty_timer = 0
            level += 1
            fall_speed -= (fall_speed - max_speed) * 0.05


        if fall_timer > fall_speed/100:
            fall_timer = 0
            current_block.deviation_y(1)
            if not(valid_space(current_block, grid, game_settings.field_width, game_settings.field_height)) and current_block.get_y() > 0:
                current_block.deviation_y(-1)
                change_block = True
        if game_settings.game_mode:
            game_ai.ai_move()
        current_block = block_controller.event_handler(win,current_block,grid, score)
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
            current_block.set_pos(game_settings.field_width//2, 0) 
            next_block = BlockFactory().create_block(random.randrange(rand_range))
            change_block = False
            score += clear_rows(grid, locked_positions)
            if game_settings.game_mode:
                game_ai.tetris_ai_loop(grid=grid,width = game_settings.field_width, height = game_settings.field_height, current_block = current_block, locked_blocks= locked_positions) 

        draw_window(win, grid, game_settings.field_width, game_settings.field_height, score = score, game_level=level, play_mode= game_settings.extended, game_mode= game_settings.game_mode)
        draw_next_shape(next_block, win, game_settings.field_width, game_settings.field_height)
        pygame.display.update()

        if check_lost(locked_positions):
            draw_message(win, "GAME OVER!", 85, (255,255,255))
            pygame.display.update()
            pygame.time.delay(2000)
            run = False
            check_top_score(score, win)
    pygame.display.quit
    mixer.music.stop()

