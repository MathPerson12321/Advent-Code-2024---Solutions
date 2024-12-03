vals = open("vals.in","r")
array = []
for i in range(0,1000):
    a = vals.readline().strip()
    if(a != ""):
        array.append(a)
amounttrue = 0

def check(data,increasing,j):
    if(increasing):
        if(data[j-1] < data[j] and (abs(data[j-1]-data[j])<=3 and abs(data[j-1]-data[j])>=1)):
            return True
    else:
        if(data[j-1] > data[j] and (abs(data[j-1]-data[j])<=3 and abs(data[j-1]-data[j])>=1)):
            return True
    return False

for i in range(0,len(array)):
    array3,array2 = array[i].split(" "),[]
    for x in range(0,len(array3)):
        array2.append(int(array3[x]))
    increasing = array2[0] < array2[1]
    fully = True
    for j in range(1,len(array2)):
        b = check(array2,increasing,j)
        if(fully):
            fully = b
    if(fully):
        amounttrue += 1
    else:
        array3 = []
        for x in range(0,len(array2)):
            array3.append(array2[x])
        for j in range(0,len(array3)):
            val = array3[j]
            array3.pop(j)
            increasing = array3[0] < array3[1]
            fully = True
            for a in range(1,len(array3)):
                b = check(array3,increasing,a)
                if(fully):
                    fully = b
            array3.insert(j,val)
            if(fully):
                amounttrue += 1
                break
print(amounttrue)