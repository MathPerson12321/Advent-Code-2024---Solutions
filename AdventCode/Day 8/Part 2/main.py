from itertools import combinations
import re

vals = open("values.in", "r")
horiz = []
for i in range(0, 50):
    horiz.append(vals.readline().strip())
antis = []
freqs = [
]  #Positions for each freqname, 3d array, like [[[3,2],[6,3]],[[7,3]]]
freqnames = []
for i in horiz:
    for j in list(i):
        if (j != "."):
            if (freqnames.count(j) == 0):
                freqnames.append(j)
                freqs.append([[horiz.index(i), list(i).index(j)]])
            else:
                freqs[freqnames.index(j)].append(
                    [horiz.index(i), list(i).index(j)])
def check(pos):
    if pos[0] >= 0 and pos[0] < len(
        horiz) and pos[1] >= 0 and pos[1] < len(horiz):
        return True
    return False
    
for i in freqs:
    for k in combinations(i, 2):
        slope = [k[1][0] - k[0][0], k[1][1] - k[0][1]]
        cons = k[1].copy()
        pos = cons
        if check(pos):
            antis.append(pos.copy())
        pos[0] += slope[0]
        pos[1] += slope[1]
        while check(pos):
            antis.append(pos.copy())
            pos[0] += slope[0]
            pos[1] += slope[1]
        pos = k[1].copy()
        pos[0] -= slope[0]
        pos[1] -= slope[1]
        while check(pos):
            antis.append(pos.copy())
            pos[0] -= slope[0]
            pos[1] -= slope[1]
antis2 = []
for i in antis:
    if (antis2.count(i) == 0):
        antis2.append(i)
print(len(antis2))
