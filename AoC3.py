import pathlib
import datetime
import os
time = datetime.datetime.now() 
os.chdir('./Advent of Code/2022/Advent-of-Code-2022')

score = 0

with open("AoC3.txt", encoding='UTF-8') as f:
    t = f.readlines()


t = [x.strip() for x in t]


for x in range(int((len(t)/3))):
    c1 = t[x*3]
    c2 = t[x*3+1]
    c3 = t[x*3+2]
    itemType = set(c1).intersection(c2).intersection(c3).pop()
    print (itemType)
    if itemType.islower():
        score += ord(itemType)-96
    else:
        score += ord(itemType)-38

print (score)
    

runtime  = datetime.datetime.now() - time
print (runtime)
