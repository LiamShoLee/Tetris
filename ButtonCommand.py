#Command Class for Tetris
from abc import ABC


class IButton(ABC):
   
    @staticmethod
    def execute():
            pass


class MenuInvoker(IButton):

    def __init__(self):
        self.commands= {}

    def registerCommand(self,newCommand):
        self.commands[newCommand.name] = newCommand

    def execute(self,command):
        self.commands[command].execute()


class Play_command(IButton):

    def __init__(self,game):
        self.name = "play"   
        self.game = game   
    def execute(self): 
        self.game.StartTetris

class Config_command(IButton):

    def __init__(self,gameMenu):
        self.name = "configure"
        self.game = gameMenu
    def execute(self):
        self.game.ConfigMenu()

class Score_command(IButton):

    def __init__(self,game):
        self.name = "show_score"
        self.game = game   
    def execute(self):
        self.game.print_score()


class Exit_command(IButton):

    def __init__(self,menu):
        self.name = "exit"
        self.menu = menu
    def execute(self):
        self.menu.quit_game()

class Back_command(IButton):

    def __init__(self,menu):
        self.name = "back"
        self.menu = menu
    def execute(self):
        self.menu.MainMenu()
        
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