class Block(object):
    def __init__(self):
        self.x = 5
        self.y = 0
        self.rotation = 0
        self.shape = [['.....',
                       '.....',
                       '.....',
                       '.....',
                       '.....']]
        self.color = ((0,0,0))
        
    def get_x(self): return self.x
    def get_y(self): return self.y
    def get_rotation(self): return self.rotation
    def get_shape(self): return self.shape
    def get_color(self): return self.color
    
    def deviation_x(self, delta):
        self.x += delta
    def deviation_y(self, delta):
        self.y += delta
    def rotate_shape(self, rotate):
        self.rotation += rotate

class S(Block):
    def __init__(self):
        super().__init__()
        self.shape = [['.....',
                       '.....',
                       '..00.',
                       '.00..',
                       '.....'],
                      ['.....',
                       '..0..',
                       '..00.',
                       '...0.',
                       '.....']]
        self.color = (0, 255, 0)
        
class Z(Block):
    def __init__(self):
        super().__init__()
        self.shape = [['.....',
                       '.....',
                       '.00..',
                       '..00.',
                       '.....'],
                      ['.....',
                       '..0..',
                       '.00..',
                       '.0...',
                       '.....']]
        self.color = (255, 0, 0)

class I(Block):
    def __init__(self):
        super().__init__()
        self.shape = [['..0..',
                       '..0..',
                       '..0..',
                       '..0..',
                       '.....'],
                      ['.....',
                       '0000.',
                       '.....',
                       '.....',
                       '.....']]
        self.color = (0, 255, 255)
        
class O(Block):
    def __init__(self):
        super().__init__()
        self.shape = [['.....',
                       '.....',
                       '.00..',
                       '.00..',
                       '.....']]
        self.color = (255, 255, 0)

class J(Block):
    def __init__(self):
        super().__init__()
        self.shape = [['.....',
                        '.0...',
                        '.000.',
                        '.....',
                        '.....'],
                        ['.....',
                        '..00.',
                        '..0..',
                        '..0..',
                        '.....'],
                        ['.....',
                        '.....',
                        '.000.',
                        '...0.',
                        '.....'],
                        ['.....',
                        '..0..',
                        '..0..',
                        '.00..',
                        '.....']]
        self.color = (0, 0, 255)

class L(Block):
    def __init__(self):
        super().__init__()
        self.shape = [['.....',
                       '...0.',
                       '.000.',
                       '.....',
                       '.....'],
                      ['.....',
                       '..0..',
                       '..0..',
                       '..00.',
                       '.....'],
                      ['.....',
                       '.....',
                       '.000.',
                       '.0...',
                       '.....'],
                      ['.....',
                       '.00..',
                       '..0..',
                       '..0..',
                       '.....']]
        self.color = (255, 165, 0)

class T(Block):
    def __init__(self):
        super().__init__()
        self.shape = [['.....',
                       '..0..',
                       '.000.',
                       '.....',
                       '.....'],
                      ['.....',
                       '..0..',
                       '..00.',
                       '..0..',
                       '.....'],
                      ['.....',
                       '.....',
                       '.000.',
                       '..0..',
                       '.....'],
                      ['.....',
                       '..0..',
                       '.00..',
                       '..0..',
                       '.....']]
        self.color = (128, 0, 128)
    
class SI(Block):
    def __init__(self):
        super().__init__()
        self.shape = [['.....',
                       '..0..',
                       '..0..',
                       '..0..',
                       '.....'],
                      ['.....',
                       '.000.',
                       '.....',
                       '.....',
                       '.....']]
        self.color = (0, 189, 0)

class SL(Block):
    def __init__(self):
        super().__init__()
        self.shape = [['.....',
                       '..0..',
                       '.00..',
                       '.....',
                       '.....'],
                      ['.....',
                       '..0..',
                       '..00.',
                       '.....',
                       '.....'],
                      ['.....',
                       '.....',
                       '..00.',
                       '..0..',
                       '.....'],
                      ['.....',
                       '.....',
                       '.00..',
                       '..0..',
                       '.....']]
        self.color = (255, 51, 255)
        
class BlockFactory:
    def create_block(self, number):
        match number:
            case 0:
                return S()
            case 1:
                return Z()
            case 2:
                return I()
            case 3:
                return O()
            case 4:
                return J()
            case 5:
                return L()
            case 6:
                return T()
            case 7:
                return SI()
            case 8:
                return SL()