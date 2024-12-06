import re
vals = open("values.in","r")
str = ""
for i in range(0,6):
    str += vals.readline().strip()
leng = len(str)
product = 0
# Regular expression to find all instances of mul(x,y)
pattern = 'mul\(\d+,\d+\)'
pattern2 = 'do\(\)'
pattern3 = "don\'t\(\)"

matches = re.findall(pattern,str)
matchesdo = re.findall(pattern2,str)
matchesdont = re.findall(pattern3,str)
doindex,dontindex = [0],[leng-1]
for j in matchesdo:
    doindex.append(str.index(j))
    str = str[:str.index(j)]+str[str.index(j)+1:]
    
for j in matchesdont:
    dontindex.append(str.index(j))
    str = str[:str.index(j)]+str[str.index(j)+1:]
    
doindex.sort()
dontindex.sort()
truearray = []
highestdont = 0
highestdo = 1
highindex = 1
for i in range(0,dontindex[0]):
    truearray.append(True)
for i in range(dontindex[0],leng):
    highindex = len(truearray)-1
    true = truearray[highindex]
    if true:
        if(i>dontindex[highestdont] and i < doindex[highestdo]):
            truearray.append(False)
            while(highestdo < len(doindex)):
                if(doindex[highestdo] < doindex[highestdo]):
                    highestdo += 1
                else:
                    break
        else:
            truearray.append(True)
    else:
        if(i>dontindex[highestdont] and i < doindex[highestdo]):
            truearray.append(False)
        else:
            while(highestdont < len(dontindex)):
                if(dontindex[highestdont] < doindex[highestdo]):
                    highestdont += 1
                else:
                    break
            truearray.append(True)

def productf(i):
    i.pop(0)
    i.pop(0)
    i.pop(0)
    i.pop(0)
    num1 = ""
    while i[0].isdigit():
        num1 += i[0]
        i.pop(0)
    i.pop(0)
    num2= ""
    while i[0].isdigit():
        num2+= i[0]
        i.pop(0)
    return (int(num1)*int(num2))

# Find all matches in the string
matches = re.findall(pattern,str)
for j in matches:
    i = list(j)
    index = str.index(j)
    if(truearray[index]):
        product += productf(i)
print(product)