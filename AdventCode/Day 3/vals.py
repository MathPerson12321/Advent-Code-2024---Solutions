import re
vals = open("values.in","r")
for i in range(0,6):
    str += vals.readline().strip()
product = 1
# Regular expression to find all instances of mul(x,y)
pattern = 'mul\(\d+,\d+\)'

# Find all matches in the string
matches = re.findall(pattern,str)
for j in matches:
    i = list(j)
    i.pop(0)
    i.pop(0)
    i.pop(0)
    i.pop(0)
    num1 = ""
    while i[0].isdigit():
        num1 += i[0]
        i.pop(0)
    i.pop(0)
    num2= ""
    while i[0].isdigit():
        num2+= i[0]
        i.pop(0)
    product += int(num1)*int(num2)
print(product)