vals = open("vals.in","r")
array = []
for i in range(0,1377):
    array.append(vals.readline().strip())
orders = []
patterns = []
for i in range(0,array.index("")):
    orders.append(array[i].split("|"))
for i in range(array.index("")+1,len(array)):
    patterns.append(array[i])

suma = 0

def check(lis,b,c):
    if(c[0] == b): #c[0] goes before c[1], no other case
        if(c[1] in lis):
            if(lis.index(c[1]) < lis.index(c[0])): #If it is false
                return False
    return True

for a in patterns:
    fixes = 0
    lis = a.split(",") #The patterns without commas, just numbers
    for b in lis: #Current number
        for c in orders: #Orders
            if not check(lis,b,c):
                print(lis)
                print(c)
                #Correcting by swapping the 2 elements that are in the wrong order
                temp0 = lis[lis.index(c[0])] 
                temp1 = lis[lis.index(c[1])]
                lis[lis.index(c[0])] = temp1
                lis[lis.index(c[1])] = temp0
                fixes += 1
    if(fixes > 0):
        first = int((len(lis)-1)/2)
        suma += int(lis[first])
        print(lis)
        print(int(lis[first]))
        print(first)
        print()
    else: 
        print("Safe")
print(suma)