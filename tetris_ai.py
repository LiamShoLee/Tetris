from re import I





class TetrisAi:

    def __init__ (self):
        self.current_move = 0
        self.next_move = 0

    def find_block_placement(self,grid, lockedblocks):
    #finds the spot it wants to put the tile
    #possibly use genetic algorythm
        possible_placements = tetris_grid_surface(grid, lockedblocks)
        block_placement = choose_next(possible_placements)
        return block_placement


    def navigate_block(self,grid,locked_blocks,current_block):


    #simple a.i algorithm
    #place block in the lowest lockable position with most contact from left to right.
    def choose_next()

    def tetris_grid_surface
