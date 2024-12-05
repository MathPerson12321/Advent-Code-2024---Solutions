import re
vals = open("values.in","r")
horizontal = []
patterns = 0
for i in range(0,140):
    a = vals.readline().strip()
    if(a != ""):
        horizontal.append(a)
vertical = []
for i in range(0,len(horizontal)):
    string = ""
    for j in range(0,len(horizontal)):
        string += list(horizontal[j])[i]
    vertical.append(string)
patterns = 0
def check(a,b):
    if(a == "M"):
        if(b == "S"):
            return True

for i in range(1,len(horizontal)-1): #Horizontal
    for j in range(1,len(list(horizontal[0]))-1): #Vertical
        h = list(horizontal[i])[j]
        if(h == "A"):
            tLeft = list(horizontal[i-1])[j-1]
            tRight = list(horizontal[i-1])[j+1]
            bLeft = list(horizontal[i+1])[j-1]
            bRight = list(horizontal[i+1])[j+1]
            if(check(tLeft,bRight) or check(bRight,tLeft)):
                if(check(tRight,bLeft) or check(bLeft,tRight)):
                    patterns += 1
print(patterns)
