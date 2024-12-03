vals = open("vals.in","r")
array = []
start = []
end = []
for i in range(0,1000):
    array.append(vals.readline().strip())
for i in range(0,1000):
    array2 = array[i].split(" ")
    start.append(int(array2[0]))
    end.append(int(array2[3]))
start.sort()
end.sort()
total = 0
for i in range(0,1000):
    total += abs(start[i]-end[i])
print(total)