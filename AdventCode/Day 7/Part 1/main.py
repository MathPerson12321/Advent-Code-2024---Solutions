import re
import itertools
vals = open("values.in","r")
arr = []
for i in range(0,850):
    arr.append(vals.readline().strip())
count = 0
for i in arr:
    first = int(i.split(":")[0])
    i = list(i)[(len(str(first))+2):]
    nums = [""]
    combs = []
    signs = ["+","*"]
    results = []
    cd = 0
    for a in i:
        if(a == " "):
            cd += 1
            nums.append("")
        else:
            nums[cd] += a
    binarray = []
    for i in range(0,2**(len(nums)-1)):
        binary = list(bin(i))
        binary.remove("b")
        while(len(binary) != (len(nums)-1)):
            if(len(binary) > len(nums)-1):
                binary.pop(0)
            else:
                binary.insert(0,"0")
        binarray.append(binary)
    for j in binarray:
        b = ""
        for k in j:
            b += signs[int(k)]
        combs.append(b)
    res = 0
    for i in combs: #If ind=0, then we find the first operation so num1...num2, otherwise we use res to do our calculations
        lis = list(i)
        for j in range(0,len(lis)):
            num1 =  nums[j]
            num2 = nums[j+1]
            if(lis[j] == "+"):
                if(j == 0):
                    res = int(num1)+int(num2)
                else:
                    res += int(num2)
            else:
                if(j == 0):
                    res = int(num1)*int(num2)
                else:
                    res *= int(num2)
        results.append(res)  
    if results.count(first) > 0:
        count += first
print(count)