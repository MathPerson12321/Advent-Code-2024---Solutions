import re
vals = open("values.in","r")
horizontal = []
pattern1 = "XMAS"
pattern2 = "SAMX"
patterns = 0
for i in range(0,10):
    horizontal.append(vals.readline().strip())

print(horizontal)
vertical = []
for i in range(0,len(horizontal)):
    string = ""
    for j in range(0,len(horizontal)):
        string += list(horizontal[j])[i]
    vertical.append(string)
print(vertical)

for i in range(0,len(horizontal)):
    patternfound = re.findall(pattern1,horizontal[i])
    patternfound2 = re.findall(pattern2,horizontal[i])
    patterns += len(patternfound) + len(patternfound2)
print(patterns)

for i in range(0,len(vertical[0])):
    for j in range(0,len(vertical[0])-3):
        lis = vertical[i]
        if(lis[j] == "X" and lis[j+1] == "M" and lis[j+2] == "A" and lis[j+3] == "S"):
            patterns += 1
            print(lis[j]+lis[j+1]+lis[j+2]+lis[j+3])
            print(j)
            print(i)
        elif(lis[j] == "S" and lis[j+1] == "A" and lis[j+2] == "M" and lis[j+3] == "X"):  
            patterns += 1
            print(lis[j]+lis[j+1]+lis[j+2]+lis[j+3])
            print(j)
            print(i)
print(patterns)
        
init = patterns
patterns = 0
for i in range(0,len(list(horizontal[0]))): #Horizontal
    for j in range(0,len(horizontal)): #Vertical
        if(j < len(horizontal)-3 and i < len(list(horizontal[0]))-3): #Right, down
            if(list(horizontal[j])[i] == "X" and list(horizontal[j+1])[i+1] == "M" and list(horizontal[j+2])[i+2] == "A" and list(horizontal[j+3])[i+3] == "S"):
                patterns += 1
            elif(list(horizontal[j])[i] == "S" and list(horizontal[j+1])[i+1] == "A" and list(horizontal[j+2])[i+2] == "M" and list(horizontal[j+3])[i+3] == "X"):
                patterns += 1
        if(j > 2 and i > 2): # Left, up
            if(list(horizontal[j])[i] == "X" and list(horizontal[j-1])[i-1] == "M" and list(horizontal[j-2])[i-2] == "A" and list(horizontal[j-3])[i-3] == "S"):
                patterns += 1
            elif(list(horizontal[j])[i] == "S" and list(horizontal[j-1])[i-1] == "A" and list(horizontal[j-2])[i-2] == "M" and list(horizontal[j-3])[i-3] == "X"):
                patterns += 1
        if(j < len(horizontal)-3 and i > 2): # Left, down
            if(list(horizontal[j])[i] == "X" and list(horizontal[j+1])[i-1] == "M" and list(horizontal[j+2])[i-2] == "A" and list(horizontal[j+3])[i-3] == "S"):
                patterns += 1
            elif(list(horizontal[j])[i] == "S" and list(horizontal[j+1])[i-1] == "A" and list(horizontal[j+2])[i-2] == "M" and list(horizontal[j+3])[i-3] == "X"):
                patterns += 1
        if(j > 2 and i < len(list(horizontal[0]))-3): # Right, up
            if(list(horizontal[j])[i] == "X" and list(horizontal[j-1])[i+1] == "M" and list(horizontal[j-2])[i+2] == "A" and list(horizontal[j-3])[i+3] == "S"):
                patterns += 1
            elif(list(horizontal[j])[i] == "S" and list(horizontal[j-1])[i+1] == "A" and list(horizontal[j-2])[i+2] == "M" and list(horizontal[j-3])[i+3] == "X"):
                patterns += 1
print(str(init+patterns))