import pathlib
import datetime
import os
time = datetime.datetime.now() 
os.chdir('./Advent of Code/2022/Advent-of-Code-2022')

with open("AoC1.txt", encoding='UTF-8') as f:
    t = f.readlines()
t = [(x.strip()) for x in t]

maxS = []
sumS = 0
for x in t:
    if x == '':
        maxS.append(sumS)
        sumS = 0
    else:
        sumS += int(x)

maxS.sort(reverse=True)
print(sum(maxS[0:3]))

runtime  = datetime.datetime.now() - time
print (runtime)
