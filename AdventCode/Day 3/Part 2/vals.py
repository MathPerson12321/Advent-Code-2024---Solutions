import re
vals = open("values.in","r")
str = ""
for i in range(0,6):
    str += vals.readline().strip()
product = 1
# Regular expression to find all instances of mul(x,y)
pattern = 'mul\(\d+,\d+\)'
pattern2 = 'do\(\)'
pattern3 = "don\'t\(\)"

matches = re.findall(pattern,str)
matchesdo = re.findall(pattern2,str)
matchesdont = re.findall(pattern3,str)
doindex,dontindex = [0],[]

for j in matchesdo:
    doindex.append(str.index(j))
    str = str[:str.index(j)]+str[str.index(j)+1:]
    
for j in matchesdont:
    dontindex.append(str.index(j))
    str = str[:str.index(j)]+str[str.index(j)+1:]
    
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
print(matchesdo)
print(matchesdont)
print(doindex)
for j in matches:
    i = list(j)
    index = matches.index(j)
    greatest = 0
    least = 0
    for a in range(0,len(matchesdo)):
        if(a < index):
            greatest = a
    inda = doindex.index(greatest)
    for a in range(0,len(matchesdont)):
        if(dontindex[a] > inda):
            least = a
    if(index >= int(greatest) and index <= int(least)):
        product += productf(i)
print(product)