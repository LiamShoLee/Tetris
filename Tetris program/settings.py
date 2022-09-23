#Settings class for tetris
#field heigh and width are int,level is int, extend is bool, game mode is bool

#from logging import _Level
#from turtle import width


class GameSettings:
    default_height = 20
    default_width = 10
    default_level = 0
    default_extend = False
    default_mode = False

    def __init__(self):
        self.set_defaults()

    def set_defaults(self):
        self.field_height = GameSettings.default_height
        self.field_width = GameSettings.default_width
        self.game_start_level = GameSettings.default_level
        self.extended = GameSettings.default_extend
        self.game_mode = GameSettings.default_mode
        return
    
    def adjust_height(self,delta):
        self.field_height += delta  
        return

    def adjust_width(self,delta):
        self.field_width += delta
        return 

    def adjust_level(self,delta):
        self.game_start_level += delta
        return

    def set_extended(self,extended_bool):
        self.extended = extended_bool
        return
        
    def set_game_mode(self,game_bool):
        self.game_mode = game_bool
        return