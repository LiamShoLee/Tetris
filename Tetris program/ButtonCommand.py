#Command Class for Tetris
from abc import ABC


class IButton(ABC):
   
    @staticmethod
    def execute():
            pass


class CommandController(IButton):

    def __init__(self):
        self.command_dict= {}

    def register_command(self,newCommand,command_key):
        self.command_dict.update({command_key : newCommand})

    def execute(self,command_key):
        self.command_dict[command_key].execute()


class PlayCommand(IButton):

    def __init__(self,game_menu): 
        self.game_menu = game_menu   

    def execute(self): 
        self.game_menu.start_tetris()

class ConfigCommand(IButton):

    def __init__(self,game_menu):
        self.game_menu = game_menu

    def execute(self):
        self.game_menu.config_menu()

class ScoreCommand(IButton):

    def __init__(self,game_menu):
        self.game_menu = game_menu   

    def execute(self):
        self.game_menu.print_score()


class ExitCommand(IButton):

    def __init__(self,game_menu):
        self.game_menu = game_menu

    def execute(self):
        self.game_menu.exit_menu()

class BackCommand(IButton):

    def __init__(self,game_menu):
        self.game_menu = game_menu

    def execute(self):
        self.game_menu.main_menu()
        
class FieldHeightPlusCommand(IButton):

    def __init__(self,settings):
        self.settings = settings

    def execute(self):
        self.settings.adjust_height(1)



class FieldHeightMinusCommand(IButton):

    def __init__(self,settings):
        self.settings=  settings

    def execute(self):
        self.settings.adjust_height(-1)

class FieldWidthPlusCommand(IButton):

    def __init__(self,settings):
        self.settings = settings

    def execute(self):
        self.settings.adjust_width(1)

class FieldWidthMinusCommand(IButton):

    def __init__(self,settings):
        self.settings = settings
    def execute(self):
        self.settings.adjust_width(-1)

class ExtendedCommand(IButton):

    def __init__(self,settings):
        self.settings = settings

    def execute(self):
            self.settings.set_extended(1)

class NormalCommand(IButton):

    def __init__(self,settings):
        self.settings = settings

    def execute(self):
            self.settings.set_extended(0)


class AiCommand(IButton):

    def __init__(self,settings):
        self.settings = settings

    def execute(self):
        self.settings.set_game_mode(1)

class PlayerCommand(IButton):

    def __init__(self,settings):
        self.settings = settings

    def execute(self):
        self.settings.set_game_mode(0)

class PlusLevelCommand(IButton):

    def __init__(self,settings):
        self.settings = settings

    def execute(self):
        self.settings.adjust_level(1)

class MinusLevelCommand(IButton):

    def __init__(self,settings):
        self.settings = settings

    def execute(self):
        self.settings.adjust_level(-1)

class ResetSettings(IButton):
    def __init__(self,settings):
        self.settings = settings
    
    def execute(self):
        self.settings.set_defaults()
        