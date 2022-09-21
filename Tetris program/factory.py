class Block():
    def create_object():
        pass
    def get_x():
        pass
    def get_y():
        pass
    def get_rotation():
        pass
    def get_shape():
        pass
    def get_color():
        pass
    def increment_x():
        pass
    def increment_y():
        pass
    def rotate_shape():
        pass

class S(Block):
    def __init__(self):
        self.x = 5
        self.y = 0
        self.rotation = 0
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

    def create_object(self):
        return self
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_rotation(self):
        return self.rotation
    def get_shape(self):
        return self.shape
    def get_color(self):
        return self.color
    def increment_x(self):
        self.x += 1
    def increment_y(self):
        self.y += 1
    def rotate_shape(self):
        self.rotation += 1

class Z(Block):
    def __init__(self):
        self.x = 5
        self.y = 0
        self.rotation = 0
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
    
    def create_object(self):
        return self

class I(Block):
    def __init__(self):
        self.x = 5
        self.y = 0
        self.rotation = 0
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
        
    def create_object(self):
        return self
        
class O(Block):
    def __init__(self):
        self.x = 5
        self.y = 0
        self.rotation = 0
        self.shape = [['.....',
                       '.....',
                       '.00..',
                       '.00..',
                       '.....']]
        self.color = (255, 255, 0)
    
    def create_object(self):
        return self

class J(Block):
    def __init__(self):
        self.x = 5
        self.y = 0
        self.rotation = 0
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
    def create_object(self):
        return self

class L(Block):
    def __init__(self):
        self.x = 5
        self.y = 0
        self.rotation = 0
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

    def create_object(self):
        return self

class T(Block):
    def __init__(self):
        self.x = 5
        self.y = 0
        self.rotation = 0
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

    def create_object(self):
        return self

class SI(Block):
    def __init__(self):
        self.x = 5
        self.y = 0
        self.rotation = 0
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

    def create_object(self):
        return self

class SL(Block):
    def __init__(self):
        self.x = 5
        self.y = 0
        self.rotation = 0
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

    def create_object(self):
        return self
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