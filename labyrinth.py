# COMP9021 24T2
# Assignment 2 *** Due Monday Week 11 @ 10.00am

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# IMPORT ANY REQUIRED MODULE


class LabyrinthError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Labyrinth:
    def __init__(self, filename):
        list1 = []
        list2 = []
        list3 = []
        with open(filename, 'r') as file:
            Lines = file.readlines()
            for line in Lines:
                list1.append(line)
            
            for line in list1:
                line = line.strip()
                list2.append(line)

            list2 = [x for x in list2 if x != '']

            for index,item in enumerate(list2):
                list2[index] = ''.join(item.split())


            ##print(list2)
            for line in list2:
                list3.append(list(line))

            
            # Check if input in incorrect
            ##print('2D list',list3)
            for i in list3:
                for j in i:
                    if(j not in ['0','1', '2', '3']):
                        raise LabyrinthError('Incorrect input.')
                    else:
                        continue
            
            length_1 = len(list3[0])

            ##all rows must have same length
            for i in range(1, len(list3)):
                if(length_1 != len(list3[i])):
                    raise LabyrinthError('Incorrect input.')
            
            yDim = len(list3)
            xDim = len(list3[0])

            ## as per requiremnts
            if(yDim < 2 or yDim > 41):
                raise LabyrinthError('Incorrect input.')

            if(xDim < 2 or xDim > 31):
                raise LabyrinthError('Incorrect input.')

            ##Now check if labyrinth is not a labyrinth
            for line in list3:
                if(line[len(line)-1] in ['1','3']):
                    raise LabyrinthError('Input does not represent a labyrinth.')
            
            last_row = list3[len(list3)-1]

            for item in last_row:
                if(item in ['2','3']):
                    raise LabyrinthError('Input does not represent a labyrinth.')

        self.line = list3
        # REPLACE PASS ABOVE WITH YOUR CODE

    
    # POSSIBLY DEFINE OTHER METHODS
    
    # method which finds the number of gates
    def no_of_gates(self):

        no_of_gates = 0
        ## contains our 2D list of elements
        grid = self.line

        ## Now lets extract the first row from grid
        gates_cordinates = []
        first_row = grid[0]
        # print('first row', first_row)
        if(first_row[0] == '0'):
            no_of_gates += 2
            gates_cordinates.append([0,0])
            gates_cordinates.append([0,0])
        if(first_row[0] == '1' or first_row[0] == '2'):
            # print('ok')
            no_of_gates += 1
            gates_cordinates.append([0,0])
            # print(no_of_gates)
        if(first_row[len(first_row)-1] == '0'):
            # print('ok2')
            no_of_gates += 1
            gates_cordinates.append([0,len(first_row)-2])
            # print(no_of_gates)
        
        ## Now lets extract the last row

        last_row_index = len(grid)-1
        last_row = grid[len(grid)-1]
        ##print('Last Row', last_row)
        for i,item in enumerate(last_row):
            if(i == len(last_row)-1):
                break
            if(item == '0'):
                no_of_gates += 1
                gates_cordinates.append([last_row_index-1,i])

        # for the 0 at the bottom right corner of 
        # the grid we counted 1 extra gate in last loop
        # no_of_gates -= 1

        ## now loop through first row 2nd elemnt till 2nd last element

        for i in range(1, len(first_row)-1):
            if(first_row[i] == '0' or first_row[i] == '2'):
                no_of_gates += 1
                gates_cordinates.append([0,i])

        ## now loop through 2nd row till 2nd last row 
        ## Only check there first elment and last element
        ## if first elemnt is 1 or 0, gate+=1
        ## if last elment is 0 gate += 1
        for ind, row in enumerate(grid):
            if(ind == len(grid)-1 or ind == 0):
                continue
            else:
                if(row[0] == '1' or row[0] == '0'):
                    no_of_gates += 1
                    gates_cordinates.append([ind,0])
                if(row[len(row)-1] == '0'):
                    no_of_gates += 1
                    gates_cordinates.append([ind, len(row)-2])
        
        gates_cordinates = sorted(gates_cordinates, key=lambda x: (x[0], x[1]))
        ##print('Gates', no_of_gates)

        #now from gate cordiantes remove the gate in which y value is len(grid[0])-1
        # for index,item in enumerate(gates_cordinates):
        #     if(item[1] == len(grid[0]) - 1 ):
        #         gates_cordinates.remove(item)
        
        self.gates = no_of_gates 
        self.gates_cordinates = gates_cordinates
        return no_of_gates

    # method which finds the set of walls
    def set_of_walls(self):

        grid = self.line

        cols = len(grid[0])
        rows = len(grid)

        visitedGrid = [[False for i in range(cols)] for j in range(rows)]
        ##print(visitedGrid)
        set_of_walls = 0

        # so start at the first not visited cell i.e 0,0
        # a cell is connected to its right cell if it itself contains 1 or 3
        # a cell is connected to its top cell if the cell at the top is 2 or 3
        # a cell is connected to its left cell if the cell at the left is 1 or 3
        # a cell is connected to its bottom cell if it itself contains 2 or 3

        # whenever the stack gets empty, the set of walls is incremented by 1

        def isValid(row,col):

            ## check if cordinate is out of bounds
            if(int(row) >= rows or int(row) < 0  or int(col) >= cols or int(col) < 0):
                return False

            #check if cordinate has been visted before
            if(visitedGrid[int(row)][int(col)] == True):
                return False
            
            #else you visit the cordiante
            return True
        
        for i_index,i in enumerate(visitedGrid):
            for j_index in range(len(grid[0])):
                #enter the first False (unvisted item) and only if its 1,2,3
                if(visitedGrid[i_index][j_index] == False  and grid[i_index][j_index] != '0'):

                    stack = []
                    stack.append([i_index,j_index])

                    while( len(stack) > 0):

                        curr = stack.pop()
                        i1 = curr[0]
                        j1 = curr[1]

                        if(isValid(i1,j1) == False):
                            continue

                        visitedGrid[i1][j1] = True
                        
                        #current cell is connected to its right
                        #cant move right if ur in last column of grid
                        if(j1+1 < len(grid[0])):

                            if(grid[i1][j1] == '1' or grid[i1][j1] == '3'):

                                if(visitedGrid[i1][j1+1] == False):
                                    stack.append([i1,j1+1])
                        
                        #current cell is connected to it top
                        #cant check top if ur in first row of grid
                        if(i1-1 >= 0):

                            if(grid[i1-1][j1] == '2' or grid[i1-1][j1] == '3'):
                                
                                if(visitedGrid[i1-1][j1] == False):
                                    stack.append([i1-1, j1])

                        #current cell is connected to its left
                        #cant check left if ur in first column of grid
                        if(j1-1 >= 0):

                            if(grid[i1][j1-1] == '1' or grid[i1][j1-1] == '3' ):
                                
                                if(visitedGrid[i1][j1-1] == False):
                                    stack.append([i1, j1-1])
                        
                        #current cell is connected to its bottom cell
                        #can check bottom cell if ur in last row og grid
                        if(i1+1 < len(grid)):

                            if(grid[i1][j1] == '2' or grid[i1][j1] == '3'):

                                if(visitedGrid[i1+1][j1] == False):
                                    stack.append([i1+1, j1])

                    set_of_walls += 1

        self.setOfWalls = set_of_walls         
        


    def innaccesible_Points(self):

        grid = self.line
        entry_points = self.gates_cordinates

        cols = len(grid[0])
        rows = len(grid)

        visitedGrid = [[False for i in range(cols)] for j in range(rows)]

        def isValid(row,col):

            ## check if cordinate is out of bounds
            if(int(row) >= rows or int(row) < 0  or int(col) >= cols or int(col) < 0):
                return False

            #check if cordinate has been visted before
            if(visitedGrid[int(row)][int(col)] == True):
                return False
            
            #else you visit the cordiante
            return True

        for e_point in entry_points:

            #extract an entry point
            row_start = e_point[0]
            col_start = e_point[1]
            
            #check if entry point is valid (i.e. is it in bound and not visited before)

            if(isValid(row_start, col_start) == False):
                continue

            # initalize a stack and push the first entry point onto it

            stack = []
            stack.append([row_start, col_start])

            while(len(stack) > 0):

                current_item = stack.pop()

                ##print('ok', current_item)
                row = int(current_item[0])
                col = int(current_item[1])

                #check if its valid:
                if(isValid(int(row), int(col)) == False):
                    continue

                # mark it as visted if its not been visted before

                visitedGrid[int(row)][int(col)] = True

                #If its valid then we shall now push valid path cordinates onto the stack1
                
                #can we move to the right i.e to its right neighbour
                #only if cell next to it contains 0 or 1
                
                #you can only move right if the next col is less than last col
                if(col + 1 < cols - 1):
                    if(grid[row][col+1] == '0' or  grid[row][col+1] == '1' ):
                    
                            stack.append([row, col+1])

                #Can we move Down 
                #only if the cell below is 0 or 2 

                #you can only move down if the cell below is not the last row
                #i.e row+1 is less than rows - 1
                if(row + 1 < rows - 1):
                    if(grid[row+1][col] == '0' or  grid[row+1][col] == '2' ):
                        
                            stack.append([row+1, col])

                #Can we move left
                #only if current cell is 0 or 1 
                if(grid[row][col] == '0' or  grid[row][col] == '1' ):

                        stack.append([row, col-1])

                #can we move up
                #only if current cell is 0 or 2

                if(grid[row][col] == '0' or grid[row][col] == '2'):
                    
                        stack.append([row-1, col])


        ## to find the number of innacessible points just loop through visited grid and
        ## chek how many Falses you get (dont loop last row and last col as they never
        ## get visted)

        ##print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in visitedGrid]))
        no_of_innaccessiblbe_points = 0
        for i in range(0, len(grid)-1):
            for j in range(0, len(grid[0])-1):
                if(visitedGrid[i][j] == False):
                    no_of_innaccessiblbe_points += 1


        self.innAccPoints = no_of_innaccessiblbe_points


    def accesible_paths(self):

        no_of_paths = 0
        grid = self.line
        entry_points = self.gates_cordinates

        cols = len(grid[0])
        rows = len(grid)


        visitedGrid = [[False for i in range(cols-1)] for j in range(rows-1)]

        def isValid(row,col):

            ## check if cordinate is out of bounds
            if(int(row) >= rows-1 or int(row) < 0  or int(col) >= cols-1 or int(col) < 0):
                return False

            #check if cordinate has been visted before
            if(visitedGrid[int(row)][int(col)] == True):
                return False
            
            #else you visited the cordiante
            return True
        
        ## loop thru the entry points 
        ## if u start at an entry point that has been visited continue to next entry gate   
        ## however if u start at an entry point and it hasnt been visted enter it 
        ## Increment the no of accesible paths by 1 each time u enter a valid entry point 
        ## keep moving forward according to value in cells
        for entryPoint in entry_points:

            ## extract the entry points cordinates 

            row = entryPoint[0]
            col = entryPoint[1]

            # go to next entry point if current entry point isnt valid
            if(isValid(row,col) == False):
                continue
            
            else:
                
                no_of_paths += 1

                stack = []
                stack.append([row,col])

                while(len(stack) > 0):

                    current = stack.pop()

                    row = current[0]
                    col = current[1]

                    if(isValid(row,col) == False):
                        continue

                    visitedGrid[int(row)][int(col)] = True

                    #If its valid then we shall now push valid path cordinates onto the stack1
                    
                    #can we move to the right i.e to its right neighbour
                    #only if cell next to it contains 0 or 1
                    
                    #you can only move right if the next col is less than last col
                    if(col + 1 < cols - 1):
                        if(grid[row][col+1] == '0' or  grid[row][col+1] == '1' ):
                        
                                stack.append([row, col+1])

                    #Can we move Down 
                    #only if the cell below is 0 or 2 

                    #you can only move down if the cell below is not the last row
                    #i.e row+1 is less than rows - 1
                    if(row + 1 < rows - 1):
                        if(grid[row+1][col] == '0' or  grid[row+1][col] == '2' ):
                            
                                stack.append([row+1, col])

                    #Can we move left
                    #only if current cell is 0 or 1 
                    if(grid[row][col] == '0' or  grid[row][col] == '1' ):

                            stack.append([row, col-1])

                    #can we move up
                    #only if current cell is 0 or 2

                    if(grid[row][col] == '0' or grid[row][col] == '2'):
                        
                            stack.append([row-1, col])

        self.no_of_paths = no_of_paths

    def set_of_cds(self):

        grid = self.line
        entry_points = self.gates_cordinates

        cols = len(grid[0])
        rows = len(grid)

        visitedGrid = [[False for i in range(cols)] for j in range(rows)]

        deadEnds = []
        def isValid(row,col):

            ## check if cordinate is out of bounds
            if(int(row) >= rows-1 or int(row) < 0  or int(col) >= cols-1 or int(col) < 0):
                return False

            #check if cordinate has been visted before
            if(visitedGrid[int(row)][int(col)] == True):
                return False
            
            #else you visited the cordiante
            return True
        
        for entryPoint in entry_points:
            ## extract the entry points cordinates 

            row = entryPoint[0]
            col = entryPoint[1]

            # go to next entry point if current entry point isnt valid
            if(isValid(row,col) == False):
                continue
            
            else:

                stack = []
                stack.append([row,col])

                while(len(stack) > 0):

                    current = stack.pop()

                    row = current[0]
                    col = current[1]

                    if(isValid(row,col) == False):
                        continue

                    visitedGrid[int(row)][int(col)] = True

                    

                    #can we move to the right i.e to its right neighbour
                    #only if cell next to it contains 0 or 1
                    
                    #you can only move right if the next col is less than last col
                    

                    if(col + 1 < cols - 1):
                        if(grid[row][col+1] == '0' or  grid[row][col+1] == '1' ):
                        
                                stack.append([row, col+1])

                    #Can we move Down 
                    #only if the cell below is 0 or 2 

                    #you can only move down if the cell below is not the last row
                    #i.e row+1 is less than rows - 1
                    if(row + 1 < rows - 1):
                        if(grid[row+1][col] == '0' or  grid[row+1][col] == '2' ):
                            
                                stack.append([row+1, col])
                        
                    #Can we move left
                    #only if current cell is 0 or 1 
                    if(grid[row][col] == '0' or  grid[row][col] == '1' ):

                            stack.append([row, col-1])

                    #can we move up
                    #only if current cell is 0 or 2

                    if(grid[row][col] == '0' or grid[row][col] == '2'):
                        
                            stack.append([row-1, col])

                    #below collects the dead end points
                    if(col + 1 <= cols - 1):
                        if(row + 1 <= rows - 1):

                            if(grid[row][col] == '3'):

                                if(grid[row+1][col] == '1' or grid[row+1][col] == '3'):
                                    
                                    if(grid[row][col+1] == '0' or grid[row][col+1] == '1'):

                                        deadEnds.append([row,col])
                                
                                if(grid[row+1][col] == '0' or grid[row+1][col] == '2'):
                                    
                                    if(grid[row][col+1] == '2' or grid[row][col+1] == '3'):

                                        deadEnds.append([row,col])

                            if(grid[row][col] == '1'):

                                if(grid[row+1][col] == '1' or grid[row+1][col] == '3'):
                                    
                                    if(grid[row][col+1] == '2' or grid[row][col+1] == '3'):

                                        deadEnds.append([row,col])
                            
                            if(grid[row][col] == '2'):

                                if(grid[row+1][col] == '1' or grid[row+1][col] == '3'):
                                    
                                    if(grid[row][col+1] == '2' or grid[row][col+1] == '3'):

                                        deadEnds.append([row,col])

        ##print('dead ends',deadEnds)   

        visitedGrid = [[False for i in range(cols)] for j in range(rows)]
        #Now we have the dead ends

        #loop thru the dead ends. 
        def isValid2(row,col):

            ## check if cordinate is out of bounds
            if(int(row) > rows or int(row) < -1  or int(col) > cols or int(col) < -1):
                return False

            #check if cordinate has been visted before
            if(visitedGrid[int(row)][int(col)] == True):
                return False
            
            #else you visited the cordiante
            return True
        for dead_point in deadEnds:

            #extract the dead end points cordinates

            row = dead_point[0]
            col = dead_point[1]

            stack = []
            stack.append([row,col])

            while (len(stack) > 0):
                current = stack.pop()

                row = current[0]
                col = current[1]
                
                visitedGrid[int(row)][int(col)] = True
                
                #can we move to the right i.e to its right neighbour
                #only if cell next to it contains 0 or 1
                
                #you can only move right if the next col 
                
                if(col + 1 <= cols - 1):
                    if(grid[row][col+1] == '0' or  grid[row][col+1] == '1' ):

                            if(isValid2(row, col+1)):
                                stack.append([row, col+1])
                #Can we move Down 
                #only if the cell below is 0 or 2 
                #you can only move down if the cell below is not out of bound
                #i.e row+1 is less than rows - 1
                if(row + 1 <= rows - 1):
                    if(grid[row+1][col] == '0' or  grid[row+1][col] == '2' ):

                            if(isValid2(row+1,col)):
                                stack.append([row+1, col])
                    
                #Can we move left
                #only if current cell is 0 or 1 
                if(grid[row][col] == '0' or  grid[row][col] == '1' ):
                        
                        if(isValid2(row,col-1)):
                            stack.append([row, col-1])
                #can we move up
                #only if current cell is 0 or 2
                if(grid[row][col] == '0' or grid[row][col] == '2'):

                        if(isValid2(row-1, col)):
                            stack.append([row-1, col])
                
                #check if current point is a gate and how many gates it has
                no_of_gates = 0

                for gate in entry_points:

                    gate_row = gate[0]
                    gate_col = gate[1]

                    if(gate_row == row and gate_col == col):
                        no_of_gates += 1
                
                if(no_of_gates >= 2):
                    visitedGrid[row][col] = False
                    break
                
                if(no_of_gates == 1 and len(stack) >= 2):
                    visitedGrid[row][col] = False
                    break

                if(no_of_gates == 1 and len(stack) <= 1 ):
                    break

                if(len(stack) >= 2):
                    visitedGrid[row][col] = False
                    break

        # Remove the last row
        visitedGrid = visitedGrid[:-1]

        # Remove the last column
        visitedGrid = [row[:-1] for row in visitedGrid]
        ##print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in visitedGrid]))

        cds_Grid = visitedGrid.copy()

        # start at a dead end point
        # extract its points
        # check if its valid
        # then check in which directions you can move
        # get a point and check if its valid and True in cds_Grid
        # if it is then put it into the stack
        # every time your stack gets empty, increment the set_of_cds by 1

        visitedGrid = [[False for i in range(cols-1)] for j in range(rows-1)]

        set_of_cds = 0
        
        for dead_end in deadEnds:
            
            row = dead_end[0]
            col = dead_end[1]

            if(not isValid(row,col)):
                continue

            stack = []
            stack.append([row,col])
            while (len(stack) > 0):
                current = stack.pop()
                row = current[0]
                col = current[1]

                visitedGrid[int(row)][int(col)] = True
                #can we move to the right i.e to its right neighbour
                #only if cell next to it contains 0 or 1
                
                #you can only move right if the next col is less than last col
            
                if(col + 1 < cols - 1):
                    if(grid[row][col+1] == '0' or  grid[row][col+1] == '1'):
                            if(cds_Grid[row][col+1] == True and isValid(row, col+1)):
                                stack.append([row, col+1])
                #Can we move Down 
                #only if the cell below is 0 or 
                #you can only move down if the cell below is not the last row
                #i.e row+1 is less than rows - 1
                if(row + 1 < rows - 1):
                    if(grid[row+1][col] == '0' or  grid[row+1][col] == '2'):
                            if(cds_Grid[row+1][col] == True and isValid(row+1,col)):
                                stack.append([row+1, col])
                    
                #Can we move left
                #only if current cell is 0 or 1 
                if(grid[row][col] == '0' or  grid[row][col] == '1'): 
                        if(cds_Grid[row][col - 1] == True and isValid(row, col-1)):
                            stack.append([row, col-1])
                #can we move up
                #only if current cell is 0 or
                if(grid[row][col] == '0' or grid[row][col] == '2'):
                        if(cds_Grid[row-1][col] == True and isValid(row-1,col)):
                            stack.append([row-1, col])
            set_of_cds += 1            
                        
        self.set_of_Cds = set_of_cds
        self.cdsGrid = cds_Grid

    def entry_exit_paths(self):

        grid = self.line
        entry_points = self.gates_cordinates
        cds_Grid = self.cdsGrid

        no_of_entry_exit_paths = 0

        cols = len(grid[0])
        rows = len(grid)

        visitedGrid = [[False for i in range(cols-1)] for j in range(rows-1)]

        def isValid(row,col):

            ## check if cordinate is out of bounds
            if(int(row) >= rows-1 or int(row) < 0  or int(col) >= cols-1 or int(col) < 0):
                return False

            #check if cordinate has been visted before
            if(visitedGrid[int(row)][int(col)] == True):
                return False
            
            #else you visited the cordiante
            return True
        
        mainPath = []
        for entryPoint in entry_points:
            
            visitedGrid = [[False for i in range(cols-1)] for j in range(rows-1)]
            ## extract the entry points cordinates 

            row = entryPoint[0]
            col = entryPoint[1]

            # go to next entry point if current entry point isnt valid
            if(isValid(row,col) == False):
                continue
            
            else:
                
                stack = []
                stack.append([row,col])

                exitFlag = True
                path = []
                while(len(stack) > 0):

                    current = stack.pop()

                    row = current[0]
                    col = current[1]

                    visitedGrid[int(row)][int(col)] = True

                    #point is a cul de sac
                    if(cds_Grid[row][col] == True):
                         exitFlag = False
                         break

                    #If its valid then we shall now push valid path cordinates onto the stack1
                    
                    #can we move to the right i.e to its right neighbour
                    #only if cell next to it contains 0 or 1
                    
                    #you can only move right if the next col is less than last col
                    if(col + 1 < cols - 1):
                        if(grid[row][col+1] == '0' or  grid[row][col+1] == '1' ):

                                if(cds_Grid[row][col+1] == False and isValid(row, col+1)):
                                    stack.append([row, col+1])

                    #Can we move Down 
                    #only if the cell below is 0 or 2 

                    #you can only move down if the cell below is not the last row
                    #i.e row+1 is less than rows - 1
                    if(row + 1 < rows - 1):
                        if(grid[row+1][col] == '0' or  grid[row+1][col] == '2' ):

                                if(cds_Grid[row+1][col] == False and isValid(row+1, col)):
                                    stack.append([row+1, col])

                    #Can we move left
                    #only if current cell is 0 or 1 
                    if(grid[row][col] == '0' or  grid[row][col] == '1' ):

                            if(cds_Grid[row][col-1] == False and isValid(row, col-1)):
                                stack.append([row, col-1])

                    #can we move up
                    #only if current cell is 0 or 2

                    if(grid[row][col] == '0' or grid[row][col] == '2'):

                            if(cds_Grid[row-1][col] == False and isValid(row-1, col)):
                                stack.append([row-1, col])
                    
                    if(len(stack) >= 2):
                         exitFlag = False
                         break
                    
                    path.append([row,col])
                
                
                if(exitFlag == True):
                    mainPath.append(path)
                    path = []
                
                if(exitFlag == False):
                    exitFlag = True
                    path = []


        for item in mainPath:
             
             #get the first item of a path, its the entry gate
             current = item[0]
             e_row = current[0]
             e_col = current[1]

             temp_gate_list = entry_points.copy()
             temp_gate_list.remove([e_row, e_col])
             #print('temp gate list',temp_gate_list)
             no_of_gates = 0
             for path in item:
                  for x in temp_gate_list:
                       if(x == path):
                            no_of_gates += 1
             
             if(no_of_gates == 1):
                  no_of_entry_exit_paths += 1

        
        ##print((no_of_entry_exit_paths//2))
                  
        self.entryExitPaths = (no_of_entry_exit_paths//2) 



    def display_features(self):
        
        ##find the number features by calling their methods
        self.no_of_gates()
        self.innaccesible_Points()
        self.accesible_paths()
        self.set_of_walls()
        self.set_of_cds()
        self.entry_exit_paths()

        if(self.gates == 0):
            print('The labyrinth has no gate.')
        if(self.gates == 1):
            print('The labyrinth has a single gate.')
        if(self.gates > 1):
            print('The labyrinth has', self.gates, 'gates.')

        if(self.setOfWalls == 0):
            print('The labyrinth has no wall.')
        
        if(self.setOfWalls == 1):
            print('The labyrinth has walls that are all connected.')
        
        if(self.setOfWalls > 1):
            print('The labyrinth has', self.setOfWalls ,'sets of walls that are all connected.')

        if(self.innAccPoints == 0):
            print('The labyrinth has no inaccessible inner point.')
        
        if(self.innAccPoints == 1):
            print('The labyrinth has a unique inaccessible inner point.')
        
        if(self.innAccPoints > 1):
            print('The labyrinth has', self.innAccPoints , 'inaccessible inner points.')

        if(self.no_of_paths == 0):
            print('The labyrinth has no accessible area.')
        
        if(self.no_of_paths == 1):
            print('The labyrinth has a unique accessible area.')

        if(self.no_of_paths > 1):
            print('The labyrinth has', self.no_of_paths ,'accessible areas.')

        if(self.set_of_Cds == 0):
            print('The labyrinth has no accessible cul-de-sac.')

        if(self.set_of_Cds == 1):
            print('The labyrinth has accessible cul-de-sacs that are all connected.')
        
        if(self.set_of_Cds > 1):
            print('The labyrinth has', self.set_of_Cds ,'sets of accessible cul-de-sacs that are all connected.')
        
        if(self.entryExitPaths == 0):
             print('The labyrinth has no entry-exit path with no intersection not to cul-de-sacs.')
        
        if(self.entryExitPaths == 1):
             print('The labyrinth has a unique entry-exit path with no intersection not to cul-de-sacs.')
        
        if(self.entryExitPaths > 1):
             print('The labyrinth has', self.entryExitPaths ,'entry-exit paths with no intersections not to cul-de-sacs.')
        # REPLACE PASS ABOVE WITH YOUR CODE

fileName = input('Which file do you want to use: ')       
lab = Labyrinth(fileName)
lab.display_features()
#print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in lab.cdsGrid]))
