import time

vals = open("values.in","r")
arr = vals.readline().strip().split(" ")

def changeStones(array):
    a = 0
    start = time.time()
    for i in range(0,len(array)):
        array[i] = str(array[i])
    "".join(array).replace("0","1")
    array = list(array)
    for i in range(0,len(array)):
        array[i] = int(array[i])
    while a < len(array):
        j = array[a]
        ind = array.index(j)
        if len(list(str(j))) % 2 == 0:
            leng = len(list(str(j)))
            halfind = int(leng/2-1)
            lis = list(str(j))[:halfind+1]
            while lis[0] == "0" and len(lis) > 1:
                lis.pop(0)
            array[ind] = int(lis[0])
            array[int(ind)] = int("".join(lis))
            insertvalue = list(str(j))[halfind+1:]
            while insertvalue[0] == "0" and len(insertvalue) > 1:
                insertvalue.pop(0)
            array.insert(ind+1,int("".join(insertvalue)))
            a += 1
        else:
            array[a] = int(array[a]) * 2024
        a += 1
    print(time.time()-start)
    return array

for i in range(0,75): #25 for part 1, 75 for part 2
    print(i)
    arr = changeStones(arr.copy())
print(len(arr))