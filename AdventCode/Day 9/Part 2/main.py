vals = open("values.in", "r")
stri = list(vals.readline().strip())
arr = []
idnum = 0
lengths = []
#Very long
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
for j in range(idnum,-1,-1):
    space = 0
    length = lengths[j]
    lastdot = arr.index(".")
    lastnodot = arr.index(str(j))+int(length)-1
    for i in range(0,len(arr)):
        if(arr[i] == "."):
            space += 1
        elif space > 0:
            break
    indid = arr.index(str(j))
    if(check(space,length) and lastdot < indid):
        for i in range(lastdot,lastdot+int(length)):  
            arr[lastnodot+lastdot-i] = "."
            arr[i] = str(j)
    else:
        while not check(space,length) and lastdot + 1 != len(arr):
            indid = arr.index(str(j))
            for i in range(0,len(arr)):
                if(arr[i] == "." and i > lastdot):
                    lastdot = i
                    break
            a = lastdot
            for i in range(lastdot,len(arr)):
                if(arr[i] == "." and i > int(a)):
                    a = i
                elif(i > int(a)):
                    break
            space = a-int(lastdot)+1
        if(lastdot + 1 != len(arr) and lastdot < indid):
            for i in range(lastdot,lastdot+int(length)):  
                arr[lastnodot+lastdot-i] = "."
                arr[i] = str(j)
sum = 0
for i in range(0,len(arr)):
    if(arr[i] != "."):
        sum += i*int(arr[i])   
print(sum)
            