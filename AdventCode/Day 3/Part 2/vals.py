import re
splitted = open("vals.in","r").read()
splitted = re.split("(do\(\)|don\'t\(\))",splitted)
count = 0
enabled = True
currents = re.findall('mul\(\d+,\d+\)',splitted[0])
for a in currents:
    nums = re.findall('\d+',a)
    count += int(nums[0])*int(nums[1])
for a in range(1,len(splitted)):
    i = splitted[a]
    if(splitted[a-1] == "do()"):
        currents = re.findall('mul\(\d+,\d+\)',i)
        for j in currents:
            nums = re.findall('\d+',j)
            count += int(nums[0])*int(nums[1])
print(count)
