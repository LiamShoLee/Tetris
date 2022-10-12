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

def main(win,settings):
    if settings.extended:
        rand_range = 9
    else:
        rand_range = 7
    level = settings.game_start_level
    flags = pygame.RESIZABLE 
    screen_width = 1070 + (settings.field_width-10)*30
    screen_height = 720 + (settings.field_height-20)*30
    win = pygame.display.set_mode((screen_width , screen_height ),flags)
    locked_positions = {}
    grid = create_grid(settings.field_width, settings.field_height, locked_positions)
    change_block = False
    run = True
    current_block = BlockFactory().create_block(random.randrange(rand_range))
    next_block = BlockFactory().create_block(random.randrange(rand_range))
    clock = pygame.time.Clock()
    difficulty_timer = 0
    fall_timer = 0
    fall_speed = 0.27 - .005 * settings.game_start_level
    removed = 0

    score = 0
    block_controller = GameController(settings.field_width,settings.field_height)
    mixer.init()
    mixer.music.load('song.wav')
    mixer.music.set_volume(0.01)
    mixer.music.play(9999)
    while run:
        grid = create_grid(settings.field_width, settings.field_height, locked_positions)
        fall_timer += clock.get_rawtime()
        difficulty_timer += clock.get_rawtime()
        volume_timer = .01
        clock.tick()

        if difficulty_timer/1000 > 10:
            difficulty_timer = 0
            volume_timer += 0.01
            mixer.music.set_volume(volume_timer)
            fall_speed -= 0.005
            level += 1


        if fall_timer/1000 > fall_speed:
            fall_timer = 0
            current_block.deviation_y(1)
            if not(valid_space(current_block, grid, settings.field_width, settings.field_height)) and current_block.get_y() > 0:
                current_block.deviation_y(-1)
                change_block = True
        
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
            next_block = BlockFactory().create_block(random.randrange(rand_range))
            change_block = False
            score += clear_rows(grid, locked_positions)

        draw_window(win, grid, score, settings.field_width, settings.field_height, game_level=level, play_mode= settings.game_mode, game_mode= settings.extended)
        draw_next_shape(next_block, win, settings.field_width, settings.field_height)
        pygame.display.update()

        if check_lost(locked_positions):
            draw_message(win, "GAME OVER!", 85, (255,255,255))
            pygame.display.update()
            pygame.time.delay(2000)
            run = False
            check_top_score(score, win)
    pygame.display.quit
    mixer.music.stop()