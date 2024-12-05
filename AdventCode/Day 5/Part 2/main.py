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
    
sum = 0
for a in patterns:
    lis = a.split(",") #The patterns without commas, just numbers
    fully = True
    for b in lis: #Current number
        for c in orders: #Orders
            if(c[0] == b): #c[0] goes before c[1], no other case
                if(c[1] in lis):
                    if(lis.index(c[1]) <= lis.index(c[0])): #If it is false
                        fully = False
                        #Correcting by swapping the 2 elements that are in the wrong order
                        temp0 = lis[lis.index(c[0])] 
                        temp1 = lis[lis.index(c[1])]
                        lis[lis.index(c[0])] = temp1
                        lis[lis.index(c[1])] = temp0
    if(fully == False):
        sum += int(lis[int((len(lis)-1)/2)])
print(sum)
