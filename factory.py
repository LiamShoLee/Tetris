class Block():
    """A class to represent a tetris block. Also a parent of serveral children block types

    Attributes:
        x: int
            x coordinate of the block
        y: int
            y coordinate of the block
        rotation: int
            rotation of the block
        shape: str arr
            array of strings that represents the different rotation of the block
        color: int tuple
            the color of the block in RGB
    
    Methods:
        get_x():
            gets the x coordinate of the block
        get_y():
            gets the y coordinate of the block
        get_rotation():
            gets the rotation of the block
        get_shape():
            gets the different forms of the block of each rotation
        get_color():
            gets the color of the block
        
        deviation_x(delta):
            changes x coordinates of the block
        deviation_y(delta):
            changes the y coordinates of the block
        rotate_shape(rotate):
            changes the rotation of the block
    """
    def __init__(self):
        """Constructs the necessary attributes for the block object
        
        Attributes:
            x: int
                x coordinate of the block
            y: int
                y coordinate of the block
            rotation: int
                rotation of the block
            shape: str arr
                array of strings that represents the different rotation of the block
            color: int tuple
                the color of the block in RGB
        """
        self.x = 2
        self.y = 0
        self.rotation = 0
        self.shape = [['.....',
                       '.....',
                       '.....',
                       '.....',
                       '.....']]
        self.color = ((0,0,0))

    def get_x(self):
        """Gets the x coordinates of the block
            
        Returns:
            self.x(int): current x coordinate        
        """
        return self.x
    def get_y(self):
        """Gets the y coordinates of the block
        
        Returns:
            self.y(int): current y coordinate 
        """
        return self.y
    def get_rotation(self):
        """Gets the rotation of the block
        
        Returns:
            self.rotation: current rotation of the shape
        """
        return self.rotation
    def get_shape(self):
        """Gets the different forms of the block of each rotation
        
        Returns:
            self.shape(str arr): array of strings representing each rotation of the block
        """
        return self.shape
    def get_color(self): 
        """Gets the color of the block
            
        Returns:
            self.color(int tup): tuple of integers representing the RGB values of the block
        """
        return self.color

    def deviation_x(self, delta):
        """Changes the x coordinate of the block
         
        Parameters:
            delta(int): either -1 or 1, which is the change in x coordinate of the block
        """
        self.x += delta
    def deviation_y(self, delta):
        """Changes the y coordinate of the block
         
        Parameters:
            delta(int): either -1 or 1, which is the change in y coordinate of the block
        """
        self.y += delta
    def rotate_shape(self, rotate):
        """Changes the rotation of the block
        
        Parameters:
            rotate(int): either -1 or 1, which is to rotate the block 
                                90 degrees anti-clockwise and clockwise respectively
        """
        self.rotation += rotate

    def set_pos(self, x_pos, y_pos):
        """ Changes the x,y coordinates of the block
         
        Parameters:
            x_pos: the new x position for the block. 
            y_pos: the new y position for the block. 
        """
        self.x = x_pos
        self.y = y_pos
        
class S(Block):
    """Child of parent block class. Represents the S block type. 
        Inherits all attributes and methods except it overrides shape and color
    """
    def __init__(self):
        """Constructs the necessary attributes for the S block object. See attributes in Block parent class."""
        super().__init__()
        self.shape = [['...',
                       '...',
                       '.00',
                       '00.'],
                      ['...',
                       '0..',
                       '00.',
                       '.0.']]
        self.color = (0,255,0) #Light green

class Z(Block):
    """Child of parent block class. Represents the Z block type. 
        Inherits all attributes and methods except it overrides shape and color
    """
    def __init__(self):
        """Constructs the necessary attributes for the Z block object. See attributes in Block parent class."""
        super().__init__()
        self.shape = [['...',
                       '...',
                       '00.',
                       '.00'
                       ],
                      ['..',
                       '.0',
                       '00',
                       '0.']]
        self.color = (255,0,0) #Red

class I(Block):
    """Child of parent block class. Represents the I block type. 
        Inherits all attributes and methods except it overrides shape and color
    """
    def __init__(self):
        """Constructs the necessary attributes for the I block object. See attributes in Block parent class."""
        super().__init__()
        self.shape = [['0',
                       '0',
                       '0',
                       '0'],
                      ['....',
                       '....',
                       '....',
                       '0000']]
        self.color = (0,255,255) #Cyan
        
class O(Block):
    """Child of parent block class. Represents the O block type. 
        Inherits all attributes and methods except it overrides shape and color
    """
    def __init__(self):
        """Constructs the necessary attributes for the O block object. See attributes in Block parent class."""
        super().__init__()
        self.shape = [['..',
                       '..',
                       '00',
                       '00']]
        self.color = (255,255,0) #Yellow

class J(Block):
    """Child of parent block class. Represents the J block type. 
        Inherits all attributes and methods except it overrides shape and color
    """
    def __init__(self):
        """Constructs the necessary attributes for the J block object. See attributes in Block parent class."""
        super().__init__()
        self.shape = [[ '...',
                        '...',
                        '0..',
                        '000'],
                        ['..',
                        '00',
                        '0.',
                        '0.'],
                        ['...',
                         '...',
                         '000',
                         '..0'],
                        ['..',
                         '.0',
                         '.0',
                         '00']]
        self.color = (0,0,255) #Navy blue

class L(Block):
    """Child of parent block class. Represents the L block type. 
        Inherits all attributes and methods except it overrides shape and color
    """
    def __init__(self):
        """Constructs the necessary attributes for the L block object. See attributes in Block parent class."""
        super().__init__()
        self.shape = [['...',
                       '...',
                       '..0',
                       '000'],
                      ['..',
                       '0.',
                       '0.',
                       '00'],
                      ['...',
                       '...',
                       '000',
                       '0..'],
                      ['..',
                       '00',
                       '.0',
                       '.0']]
        self.color = (255,165,0) #Orange

class T(Block):
    """Child of parent block class. Represents the T block type. 
        Inherits all attributes and methods except it overrides shape and color
    """
    def __init__(self):
        """Constructs the necessary attributes for the T block object. See attributes in Block parent class."""
        super().__init__()
        self.shape = [['...',
                       '...',
                       '.0.',
                       '000'],
                      ['...',
                       '0..',
                       '00.',
                       '0..'],
                      ['...',
                       '...',
                       '000',
                       '.0.'],
                      ['..',
                       '.0',
                       '00',
                       '.0']]
        self.color = (128,0,128) #Purple
    
class SI(Block):
    """Child of parent block class. Represents the small I block type. 
        Inherits all attributes and methods except it overrides shape and color.
    """
    def __init__(self):
        """Constructs the necessary attributes for the SI block object. See attributes in Block parent class."""
        super().__init__()
        self.shape = [['...',
                       '0..',
                       '0..',
                       '0..'],
                      ['...',
                       '...',
                       '...',
                       '000']]
        self.color = (0,189,0) #Dark green

class SL(Block):
    """Child of parent block class. Represents the small L block type. 
        Inherits all attributes and methods except it overrides shape and color
    """
    def __init__(self):
        """Constructs the necessary attributes for the SL block object. See attributes in Block parent class."""
        super().__init__()
        self.shape = [['..',
                       '..',
                       '.0',
                       '00'],
                      ['..'
                       '..',
                       '0.',
                       '00'],
                      ['..',
                       '..',
                       '00.',
                       '0..'],
                      ['..',
                       '..',
                       '00',
                       '.0']]
        self.color = (255,51,255) #Pink
        
class BlockFactory:
    """A class that determines which block to create
    
    Methods:
        create_block(number):
            creates a block object dependent on the given number
    """
    def create_block(self, number):
        """Creates a block dependent on the given number, and returns the corresponding block

        Parameter:
            number(int): randomly generated number

        Returns:
            Block: One of the several tetris blocks
        """
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