#Settings class for tetris
#fieldSize is (int,int),level is int, extend is bool, 

from logging import _Level
from turtle import width


class GameSettings:
    def __init__(self,default_height,default_width,default_level,default_extend,default_mode):
        self.field_height = default_height
        self.field_width = default_width
        self.game_start_Level = default_level
        self.extended = default_extend
        self.game_mode = default_mode

    def adjust_height(self,delta):
        self.field_height += delta  
        return

    def adjust_width(self,delta):
        self.field_width += delta
        return 

    def adjust_level(self,delta):
        self.game_start_Level += delta
        return

    def set_extended(self,extended_bool):
        self.extended = extended_bool
        return
        
    def set_game_mode(self,game_bool):
        self.game_mode = game_bool
        return