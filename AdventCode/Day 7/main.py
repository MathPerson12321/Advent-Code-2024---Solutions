import re
import itertools
vals = open("values.in","r")
arr = []
for i in range(0,9):
    arr.append(vals.readline().strip())
for i in arr:
    print(i)
    first = int(i.split(":")[0])
    i = list(i)[(len(str(first))+2):]
    nums = [""]
    combs = []
    signs = ["+","*"]
    cd = 0
    for a in i:
        if(a == " "):
            cd += 1
            nums.append("")
        else:
            nums[cd] += a
    print(nums)
    for i in range(0,2**(len(nums)-1)):
        binary = list(bin(i))
        binary.remove("b")
        print(binary)
        while(len(binary) > (len(nums)-1)):
            binary.pop(0)
        b = ""
        for j in range(0,len(nums)-1):
            for k in binary:
                b += signs[int(k)]
        print(b)
    print()