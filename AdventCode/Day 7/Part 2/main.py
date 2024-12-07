'''Note, Day 7 P2 is a very long challenge and the code can take minutes to run.
The code will print the line it is checking (out of the length of your puzzle input).
Note that the answer is very large.'''
import re
vals = open("values.in","r")
arr = []
for i in range(0,850):
    arr.append(vals.readline().strip())
count = 0
def tern(number):
    if number < 3:
        return list(str(number))
    digits = []
    while number:
        digits.append(number % 3)
        number //= 3
    return list(reversed(digits))

for i in arr:
    print(arr.index(i)+1)
    first = int(i.split(":")[0])
    i = list(i)[(len(str(first))+2):]
    nums = [""]
    combs = []
    signs = ["+","*","||"]
    results = []
    cd = 0
    for a in i:
        if(a == " "):
            cd += 1
            nums.append("")
        else:
            nums[cd] += a
    ternarray = []
    for j in range(0,3**(len(nums)-1)):
        ternary = tern(j)
        while(len(ternary) != (len(nums)-1)):
            if(len(ternary) > len(nums)-1):
                ternary.pop(0)
            else:
                ternary.insert(0,"0")
        ternarray.append(ternary)

    for j in ternarray:
        b = ""
        for k in j:
            b += signs[int(k)]
        combs.append(b)
    res = 0
    for k in combs: #If ind=0, then we find the first operation so num1...num2, otherwise we use res to do our calculations
        a = re.split(r'(\|\||\+|\*)', k)
        for b in range(len(a)-1,-1,-1):
            if(a[b] == ""):
                a.pop(b)
                b -= 1
        for j in range(0,len(a)):
            num1 =  nums[j]
            num2 = nums[j+1]
            if(a[j] == "+"):
                if(j == 0):
                    res = int(num1)+int(num2)
                else:
                    res += int(num2)
            elif(a[j] == "*"):
                if(j == 0):
                    res = int(num1)*int(num2)
                else:
                    res *= int(num2)
            else:
                if(j == 0):
                    res = int(num1+num2)
                else:
                    res = int(str(res)+str(num2))
        if(res == first):
          count += first
          break
print(count)