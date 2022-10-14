def get_shape_position(shape):
    """Determines which positions in the grid the current shape occupies when this function is called

    Parameters:
        shape(Block): block object containing all information regarding the block

    Returns:
        positions(tuple<int, int> arr): array of <int, int> tuples representing the 
                                        positions the current shape is on the grid
    """
    positions = []
    form = shape.get_shape()[shape.get_rotation() % len(shape.get_shape())] #Gets the shape of current rotation

    #Puts the x,y positions of the '0' character into the positions array and adjusts offset
    for i, line in enumerate(form):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j , shape.y + i - 3)) #the "-2" and "-" adjusts the offset

    return positions

def shape_flatness(shape):
    flat_score = 0
    for pos in shape:
        flat_score += pos[1]*pos[1]
    return flat_score
   

def valid_space(block, grid, width, height):
    """Checks if the space that the block is moving/rotating into is empty tile.
        If the tile is empty, then the block will proceed with its action, otherwise the block won't change to its new positions

    Parameters:
        block (Block): data for a block object
        grid (2D array of RGB tuples): data representation of the color of each tile in the grid

    Returns:
        Bool: False if any part of the current block is in an invalid tile. True otherwise
    """
    accepted_pos = [[(j, i) for j in range(width) if grid[i][j] == (0,0,0)] for i in range(height)] #Finds all empty tiles in the grid
    accepted_pos = [j for sub in accepted_pos for j in sub] #Flattens list

    shape_form = get_shape_position(block)

    #If any part of the shape is not accepted, return False
    for pos in shape_form:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True


def check_lost(positions):
    """Checks if there is any blocks above grid. If there is then the game is lost

    Parameters:
        positions (dict): dictionary of positions where blocks have been locked

    Returns:
        bool: True if the player has topped out, False otherwise
    """
    
    #Checks if there are any blocks above the grid. End game if True
    for pos in positions:
        x, y = pos
        if y < 0:
            return True

    return False