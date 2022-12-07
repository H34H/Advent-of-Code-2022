import pandas as pd
import lifelines
import os

df = pd.read_csv('../3dprinter/data.csv', delimiter=';')

df.head()
import pathlib
import datetime
import os
time = datetime.datetime.now() 
os.chdir('./Advent of Code/2022/Advent-of-Code-2022')
score = 0

def TranslateMovement(instruction):
    i = instruction.split()
    repeats = int(i[1])
    fromPile = int(i[3])-1
    toPile = int(i[5])-1
    return repeats, fromPile, toPile


with open("AoC5.txt", encoding='UTF-8') as f:
    t = f.readlines()

t = [x.strip() for x in t]
piles = t[0:8]
movements = t[10:]

stapels = []

for p in range(9):
    stapels.append('')
    for layer in range(7,-1,-1):
        stapels[-1] += (piles[layer][p*4+1])
    
stapels = [x.strip() for x in stapels]
print (stapels)

for m in movements:
    repeats, fromPile, toPile = TranslateMovement(m)
    print (repeats, fromPile, toPile)
    l = len(stapels[fromPile])
    stapels[toPile] += stapels[fromPile][l-repeats:]
    stapels[fromPile] = stapels[fromPile][:l-repeats:]

    print(stapels)
print ('---')
        
runtime  = datetime.datetime.now() - time
print (runtime)
