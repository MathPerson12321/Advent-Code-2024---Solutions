#Method: Find the regular path, for each step on that, put an obstruction, and make a list of places the person goes before changing direction. If they go there twice, it is infinite.
import re
vals = open("values.in","r")
horizontal,vertical = [],[]
for i in range(0,130):
    horizontal.append(vals.readline().strip())
obs = []
guard = []
lengthh = len(horizontal)
lengthv = len(list(horizontal[0]))

for i in range(0,lengthv):
    string = ""
    for j in range(0,lengthh):
        string += list(horizontal[j])[i]
    vertical.append(string)

for i in range(0,lengthh): #Rows
    for j in range(0,lengthv): #Columns
        if(list(horizontal[i])[j] == "#"):
            arr = [i,j]
            obs.append(arr)
        elif(list(horizontal[i])[j] == "^"):
            guard.append(i)
            guard.append(j)
            
def checkpos(guard):
    return (guard[0] < 0 or guard[0] >= lengthh or guard[1] < 0 or guard[1] >= lengthv)

def findPath(guard,obs):
    positions = []
    dir = 1 #1 = forward, 2 = right, 3 = down, 4 = left (like a compass)
    turnpoints = []
    while not checkpos(guard):
        if(dir == 1):
            if([guard[0]-1,guard[1]] not in obs): #Guard ahead
                guard[0] -= 1
                positions.append([guard[0],guard[1]])
            else:
                dir += 1
                dir = dir % 4
                turnpoints.append([[guard[0],guard[1]],dir])
        if(dir == 2):
            if([guard[0],guard[1]+1] not in obs): #Guard ahead
                guard[1] += 1
                positions.append([guard[0],guard[1]])
            else:
                dir += 1
                dir = dir % 4
                turnpoints.append([[guard[0],guard[1]],dir])
        if(dir == 3):
            if([guard[0]+1,guard[1]] not in obs): #Guard ahead
                guard[0] += 1
                positions.append([guard[0],guard[1]])
            else:
                dir += 1
                dir = dir % 4
                turnpoints.append([[guard[0],guard[1]],dir])
        if(dir == 0):
            if([guard[0],guard[1]-1] not in obs): #Guard ahead
                guard[1] -= 1
                positions.append([guard[0],guard[1]])
            else:
                dir += 1
                dir = dir % 4
                turnpoints.append([[guard[0],guard[1]],dir])
        for i in turnpoints:
            if(turnpoints.count(i) > 1):
                return False
    #print(turnpoints)
    return [positions,turnpoints]

count = 0
res = findPath(guard.copy(),obs)
poss = res[0]
'''print()
print(res)
print()'''

for i in poss:
    #print(obs)
    obs.append(i)
    '''print(i)
    print(obs)
    print()'''
    res = findPath(guard.copy(),obs)
    '''print(res)
    print()'''
    if(not res):
        '''print(obs)
        print(guard)
        print()
        print()'''
        count += 1
    obs.pop(-1)
print(count-1)