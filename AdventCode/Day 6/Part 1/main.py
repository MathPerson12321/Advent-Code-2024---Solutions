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
positions = []
dir = 1 #1 = forward, 2 = right, 3 = down, 4 = left (like a compass)

def check(guard):
    return (guard[0] < 0 or guard[0] >= lengthh or guard[1] < 0 or guard[1] >= lengthv)

while not check(guard):
    if(dir == 1):
        checkres = False
        for i in obs:
            if(guard[0]-1 == i[0] and guard[1] == i[1]): #Guard ahead
                checkres = True
        if not checkres:
            guard[0] -= 1
            positions.append([guard[0],guard[1]])
        else:
            dir += 1
            dir = dir % 4
    if(dir == 2):
        checkres = False
        for i in obs:
            if(guard[1]+1 == i[1] and guard[0] == i[0]): #Guard ahead
                checkres = True
        if not checkres:
            guard[1] += 1
            positions.append([guard[0],guard[1]])
        else:
            dir += 1
            dir = dir % 4
    if(dir == 3):
        checkres = False
        for i in obs:
            if(guard[0]+1 == i[0] and guard[1] == i[1]): #Guard ahead
                checkres = True
        if not checkres:
            guard[0] += 1
            positions.append([guard[0],guard[1]])
        else:
            dir += 1
            dir = dir % 4
    if(dir == 0):
        checkres = False
        for i in obs:
            if(guard[1]-1 == i[1] and guard[0] == i[0]): #Guard ahead
                checkres = True
        if not checkres:
            guard[1] -= 1
            positions.append([guard[0],guard[1]])
        else:
            dir += 1
            dir = dir % 4
positions2 = [guard]
for i in positions:
    if not i in positions2:
        positions2.append(i)
print(len(positions2))
                