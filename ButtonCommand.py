#Command Class for Tetris
from abc import ABC


class IButton(ABC):
   
    @staticmethod
    def execute():
            pass


class MenuInvoker(IButton):

    def __init__(self):
        self.command_dict= {}

    def registerCommand(self,newCommand,command_key):
        self.command_dict[command_key] = newCommand

    def execute(self,command_key):
        self.command_dict[command_key].execute()


class PlayCommand(IButton):

    def __init__(self,game_menu):
        self.name = "play"   
        self.game_menu = game_menu   
    def execute(self): 
        self.game_menu.StartTetris

class ConfigCommand(IButton):

    def __init__(self,game_menu):
        self.name = "configure"
        self.game_menu = game_menu
    def execute(self):
        self.game_menu.ConfigMenu()

class ScoreCommand(IButton):

    def __init__(self,game_menu):
        self.name = "show_score"
        self.game_menu = game_menu   
    def execute(self):
        self.game_menu.print_score()


class ExitCommand(IButton):

    def __init__(self,game_menu):
        self.name = "exit"
        self.game_menu = game_menu
    def execute(self):
        self.game_menu.quit_game()

class BackCommand(IButton):

    def __init__(self,game_menu):
        self.name = "back"
        self.game_menu = game_menu
    def execute(self):
        self.game_menu.MainMenu()
        
class FieldHeightPlusCommand(IButton):

    def __init__(self,settings):
        self.name = "plus_height"
        self.settings = settings
    def execute(self):
        self.settings.adjust_height(1)



class FieldHeightMinusCommand(IButton):

    def __init__(self,settings):
        self.name = "minus_height"
        self.settings=  settings
    def execute(self):
        self.settings.adjust_height(-1)

class FieldWidthPlusCommand(IButton):

    def __init__(self,settings):
        self.name = "plus_width"
    def execute(self):
        self.settings.adjust_width(1)

class FieldWidthMinusCommand(IButton):

    def __init__(self,settings):
        self.name = "minus_width"
        self.settings = settings
    def execute(self):
        self.settings.adjust_width(-1)

class ExtendedCommand(IButton):

    def __init__(self,settings):
        self.settings = settings
        self.name = "select_extended"
    def execute(self):
            self.settings.set_extended(1)

class NormalCommand(IButton):

    def __init__(self,settings):
        self.settings = settings
        self.name = "select_normal"
    def execute(self):
            self.settings.set_extended(0)


class AiCommand(IButton):

    def __init__(self,settings):
        self.settings = settings
        self.name = "select_ai"
    def execute(self):
        self.settings.set_game_mode(1)

class PlayerCommand(IButton):

    def __init__(self,settings):
        self.settings = settings
        self.name = "select_player"
    def execute(self):
        self.settings.set_game_mode(0)

class PlusLevelCommand(IButton):

    def __init__(self,settings):
        self.settings = settings
        self.name = "increment_level"
    def execute(self):
        self.settings.adjust_level(1)

class MinusLevelCommand(IButton):

    def __init__(self,settings):
        self.settings = settings
        self.name = "decrement_level"
    def execute(self):
        self.settings.adjust_level(0)