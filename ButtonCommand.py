#Command Class for Tetris
from abc import ABCMeta, abstractmethod


class IButton(metaclass = ABCMeta):
   
    @staticmethod
    @abstractmethod
    def execute():


class MenuInvoker:

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
        


class FieldHeightMinusCommand(IButton):

    def __init__(self):
        self.name = "minus_height"
    def execute(self):


class FieldWidthPlusCommand(IButton):

    def __init__(self):
        self.name = "plus_width"
    def execute(self):


class FieldWidthMinusCommand(IButton):

    def __init__(self):
        self.name = "minus_width"
    def execute(self):


class ExtendedCommand(IButton):

    def __init__(self):
        self.name = "select_extended"
    def execute(self):


class NormalCommand(IButton):

    def __init__(self):
        self.name = "select_normal"
    def execute(self):


class AiCommand(IButton):

    def __init__(self):
        self.name = "select_ai"
    def execute(self):


class PlayerCommand(IButton):

    def __init__(self):
        self.name = "select_player"
    def execute(self):


class PlusLevelCommand(IButton):

    def __init__(self):
        self.name = "increment_level"
    def execute(self):


class MinusLevelCommand(IButton):

    def __init__(self):
        self.name = "decrement_level"
    def execute(self):