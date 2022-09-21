#Settings class for tetris
#fieldSize is (int,int),level is int, extend is bool, 

class GameSettings:
    def __init__(self,defaultSize,defaultLevel,defaultExtend,defaultMode):
        self.fieldSize = defaultSize
        self.gameStartLevel = defaultLevel
        self.extended = defaultExtend
        self.gameMode = defaultMode
