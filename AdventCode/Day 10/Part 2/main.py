import numpy as np

directions = [(0,1), (1,0), (0,-1), (-1,0)] #Directions
total = 0 

def findPaths(start, height, tempGrid):
    x,y = start
    paths = 0
    for i in range(len(directions)): #From 0 to 4, 0-3 included
        dx, dy = directions[i] #Change in x,y
        if 0 <= x+dx < len(tempGrid) and 0 <= y+dy < len(tempGrid): #If adding a direction does not go out of bounds
            if int(tempGrid[x+dx,y+dy]) == height + 1: #Checking if the place on the grid after changing the direction works
                if height+1 == 9: #If we get to 9
                    paths += 1
                    #tempGrid[x+dx, y+dy] = "0"  #Uncomment for part 1, this will make it so that the program will not overcount for part 1 (we want to consider it for part 2)
                else: #For the direction pos, next num, and grid, check again for all directions using the for loop
                    paths += findPaths((x+dx, y+dy), height + 1, tempGrid)
    return paths

with open("values.in", "r") as file:
    grid = np.array([[char for char in line] for line in file.read().splitlines()]) #For each line, make a list and put it into array
    starts = np.where(grid == "0") #Where a value is 0
    starts = list(zip(starts[0], starts[1])) #Combine the 2 different arrays inside starts into a list, coordinates from row num to column num as indexes
print(starts)
for i in starts: #For each position
    tempGrid = grid.copy()
    total += findPaths(i, 0, tempGrid) #Find the number of paths from that position, with the starting array, the number, and grid
print(total)