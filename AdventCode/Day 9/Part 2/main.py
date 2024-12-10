vals = open("values.in", "r")
stri = list(vals.readline().strip())
arr = []
idnum = 0
lengths = []
dotarray = []
for i in range(0,len(stri)):
    if(i % 2 == 0):
        for j in range(0,int(stri[i])):
            arr.append(str(idnum))
        idnum += 1
        lengths.append(stri[i])
    else:
        for j in range(0,int(stri[i])):
            arr.append(".")
idnum -= 1
def check(space,length):
    return int(space) >= int(length)
space = 0

def dotarrayassign():
    dotarray = []
    space = 0
    for i in range(0,len(arr)):
        if(arr[i] == "."):
            space += 1
        elif space > 0:
            dotarray.append([space,i-space])
            space = 0
    return dotarray
    
for j in range(idnum,-1,-1):
    print(j) #To keep track of progress
    space = 0
    length = lengths[j]
    while arr[-1] == ".":
        arr.pop(-1)
    lastnodot = arr.index(str(j))+int(length)-1
    dotarray = dotarrayassign()
    indid = arr.index(str(j))
    for i in dotarray:
        space = i[0]
        if(check(space,length) and i[1] < lastnodot):
            for k in range(i[1],i[1]+int(length)):
                arr[lastnodot+i[1]-k] = "."
                arr[k] = str(j)
            break
sum = 0
for i in range(0,len(arr)):
    if(arr[i] != "."):
        sum += i*int(arr[i])   
print(sum)
            
            