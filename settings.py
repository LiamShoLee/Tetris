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
        """Resets the values of the game to the preset values of a default game
        Parameters: 
            self: changes values of current game attributes
        Return: 
            self: reset values of the GameSettings
        """

        self.field_height = GameSettings.default_height
        self.field_width = GameSettings.default_width
        self.game_start_level = GameSettings.default_level
        self.extended = GameSettings.default_extend
        self.game_mode = GameSettings.default_mode
        return
    
    def adjust_height(self,delta):
        """modifies the value of the field_height variable by a value delta
        Parameters: 
            self: to call the field_height variable and modify it
            delta: the change to field_height
        Return: 
            self: returns updated value of field_height
        """
        self.field_height += delta  
        return

    def adjust_width(self,delta):
        """modifies the value of the field_width variable by a value delta
        Parameters: 
            self: to call the field_width variable and modify it
            delta: the change to field_width
        Return: 
            self: returns updated value of field_width
        """
        self.field_width += delta
        return 

    def adjust_level(self,delta):
        """modifies the value of the adjust_level variable by a value delta
        Parameters: 
            self: to call the start_level variable and modify it
            delta: the change to start_level
        Return: 
            self: returns updated value of start_level
        """
        self.game_start_level += delta
        return

    def set_extended(self,extended_bool):
        """sets value of self.extended to updated value extended_bool 
        Parameters: 
            self: to call the extended variable in self
            extended_bool: the value to update the extended variable to
        Return: 
            self: returns updated value of extended_bool
        """
        self.extended = extended_bool
        return
        
    def set_game_mode(self,game_bool):
        """sets value of self.game_mode to updated value gane_bool 
        Parameters: 
            self: to call the game_mode variable in self
            game_bool: the value to update the game_mode to
        Return: 
            self: returns updated value of game_mode
        """
        
        self.game_mode = game_bool
        return