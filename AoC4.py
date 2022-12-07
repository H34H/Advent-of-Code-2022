import pathlib
import datetime
import os
time = datetime.datetime.now() 
os.chdir('./Advent of Code/2022/Advent-of-Code-2022')

score = 0

with open("AoC4.txt", encoding='UTF-8') as f:
    t = f.readlines()

t = [x.strip().split(',') for x in t]


for x in t:
    x = ([y.split('-') for y in x])
    section1 = set(range(int(x[0][0]), int(x[0][1])+1))
    section2 = set(range(int(x[1][0]), int(x[1][1])+1))
    if len((section1).intersection((section2)))>0 or len((section2).intersection((section1)))>0:
        #print (section1, section2)
        score += 1

print(score)
        
runtime  = datetime.datetime.now() - time
print (runtime)
