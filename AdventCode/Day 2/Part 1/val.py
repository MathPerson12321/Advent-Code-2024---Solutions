vals = open("val.in","r")
array = []
for i in range(0,1000):
    array.append(vals.readline().strip())
amounttrue = 0

def intconf(n):
    return int(n)

for i in range(0,1000):
    array3,array2 = array[i].split(" "),[]
    for x in range(0,len(array3)):
        array2.append(intconf(array3[x]))
    increasing = array2[0] < array2[1]
    fully = True
    for j in range(1,len(array2)):
        if(increasing):
            if(array2[j-1] >= array2[j] or abs(array2[j-1]-array2[j])>3):
                fully = False
        else:
            if(array2[j-1] <= array2[j] or abs(array2[j-1]-array2[j])>3):
                fully = False
    if(fully == True):
        amounttrue += 1
print(amounttrue)