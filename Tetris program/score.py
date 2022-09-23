def clear_rows(grid, locked):
    """Clears all completed lines in the game and shifts entire grid down to fill in the eliminated lines.
        Also returns the score depending on how many lines were eliminated at once

    Parameters:
        grid (2D array of RGB tuples): data representation of the color of each tile in the grid
        locked (dict): dictionary of positions where blocks have been locked

    Returns:
        int: the number of points to be awarded for clearing lines, or 0 if no lines were cleared
    """
    lines_cleared = 0
    
    #Check each lines starting from bottom of grid
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        
        if (0,0,0) not in row: #If no empty tiles in the row
            lines_cleared += 1
            index = i
            
            #Delete line from the grid
            for j in range(len(row)):
                try:
                    del locked[(j,i)]
                except:
                    continue

    #Shifts entire grid down if there are any lines eliminated
    if lines_cleared > 0:
        
        #For each row in the grid
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            
            if y < index: #Shift down current row if it was above the last eliminated line
                newKey = (x, y + lines_cleared)
                locked[newKey] = locked.pop(key)

    match lines_cleared:
        case 1:
            return 100
        case 2:
            return 300
        case 3:
            return 600
        case 4:
            return 1000
    return 0