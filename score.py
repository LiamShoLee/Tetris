import pygame
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






def check_top_score(top_score, screen):
    input_rect = pygame.Rect(200, 200, 240, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    base_font = pygame.font.SysFont('comicsans', 32)
    user_text = ''
    color = color_passive
    active = False
    scores = [line.strip('\n') 
        for line in open('scores.txt', 'r').readlines()]
    my_list = []
    flag = True
    count = 1
    for score in scores:
        sep = score.split()
        if int(sep[2]) < top_score:
            while flag:
                screen.fill((255,255,255))
                pygame.draw.rect(screen, color, input_rect)
                text_surface = base_font.render(user_text, True, (255, 255, 255))
                screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
                pygame.display.flip()
                
                if active:
                    color = color_active
                else:
                    color = color_passive
                
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if input_rect.collidepoint(event.pos):
                            active = True
                        else:
                            active = False
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        elif event.key == pygame.K_RETURN:
                            flag = False
                        else:
                            user_text += event.unicode
                    
                        
            new_score = [count,user_text, top_score]
            my_list.append(new_score)
            count += 1
            my_list.append([count, sep[1], sep[2]])
            top_score = -1
        else:
            my_list.append([count, sep[1], sep[2]])
        
        if count == 10:
            break
        count += 1

    if top_score is -1:
        f = open("scores.txt", "w")
        f.close()
        f = open("scores.txt", "a")
        for num in range(10):
            f.write(str(num+1) + " " + my_list[num][1] + " " + str(my_list[num][2])+"\n")
        f.close()