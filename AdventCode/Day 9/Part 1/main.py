vals = open("values.in", "r")
stri = list(vals.readline().strip())
arr = []
idnum = 0
for i in range(0,len(stri)):
    if(i % 2 == 0):
        for j in range(0,int(stri[i])):
            arr.append(str(idnum))
        idnum += 1
    else:
        for j in range(0,int(stri[i])):
            arr.append(".")
while "." in arr:
    if(len(arr)-arr.index(".") != arr.count(".")):
        last = ""
        for i in range(len(arr)-1,0,-1):
            if(arr[i] != "."):
                last = arr[i]
                break
        for i in range(len(arr)-1,0,-1):
            if(arr[i] != "."):
                arr[i] = "."
                break
        ind = arr.index(".")
        arr[ind] = last
    else:
        break
sum = 0
for i in range(0,arr.index(".")):
    sum += i*int(arr[i])   
print(sum)
            