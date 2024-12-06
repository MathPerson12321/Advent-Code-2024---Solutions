import re
vals = open("values.in","r")
str = ""
for i in range(0,1):
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
doindex,dontindex = [0],[len(str)-1]
for j in matchesdo:
    doindex.append(str.index(j))
    
for j in matchesdont:
    dontindex.append(str.index(j))
    
doindex.sort()
dontindex.sort()
truearray = []
highestdont = dontindex[0]
highestdo = doindex[1]
highindex = 1
print(doindex)
print(dontindex)
for i in range(0,leng):
    if(i < dontindex[0]):
        truearray.append(True)
    else:
        highindex = len(truearray)-1
        true = truearray[highindex]
        if(true):
            if(highestdont >= i):
                truearray.append(False)
                highestdont += 1
                print(i)
            else:
                truearray.append(True)
        else:
            if(highestdo <= i):
                highestdo += 1
                truearray.append(True)
                print(i)
            else:
                truearray.append(False)
print(truearray)
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
        print(i)
        product += productf(i)
print(product)