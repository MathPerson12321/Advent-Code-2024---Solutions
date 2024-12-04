import re
vals = open("values.in","r")
letters = []
pattern1 = "XMAS"
pattern2 = "SAMX"
patterns = 0
for i in range(0,140):
    letters.append(vals.readline().strip())
for i in range(0,len(letters)):
    patternfound = re.findall(pattern1,letters[i])
    patterns += len(patternfound)
for i in range(0,len(letters)):
    patternfound = re.findall(pattern2,letters[i])
    patterns += len(patternfound)
for i in range(0,len(list(letters[0]))):
    for j in range(0,len(letters)-3):
        lis = list(letters[j])
        if(lis[j] == "X" and lis[j+1] == "M" and lis[j+2] == "A" and lis[j+3] == "S"):
            patterns += 1
        elif(lis[j] == "S" and lis[j+1] == "A" and lis[j+2] == "M" and lis[j+3] == "X"):  
            patterns += 1
for i in range(0,len(list(letters[0]))-3): #Horizontal
    for j in range(0,len(letters)-3): #Vertical
        if(list(letters[j])[i] == "X" and list(letters[j+1])[i+1] == "M" and list(letters[j+2])[i+2] == "A" and list(letters[j+3])[i+3] == "S"):
            patterns += 1
        elif(list(letters[j])[i] == "S" and list(letters[j+1])[i+1] == "A" and list(letters[j+2])[i+2] == "M" and list(letters[j+3])[i+3] == "X"):
            patterns += 1
        if(list(letters[j])[i] == "X" and list(letters[j-1])[i-1] == "M" and list(letters[j-2])[i-2] == "A" and list(letters[j-3])[i-3] == "S"):
            patterns += 1
        elif(list(letters[j])[i] == "S" and list(letters[j-1])[i-1] == "A" and list(letters[j-2])[i-2] == "M" and list(letters[j-3])[i-3] == "X"):
            patterns += 1
print(patterns)