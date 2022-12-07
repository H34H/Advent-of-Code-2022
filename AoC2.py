import pathlib
import datetime
import os
time = datetime.datetime.now() 
os.chdir('./Advent of Code/2022/Advent-of-Code-2022')

with open("AoC2.txt", encoding='UTF-8') as f:
    t = f.readlines()



t = [x.strip().split(' ') for x in t]



#A for Rock => 1
#B for Paper => 2
#C for Scissors => 3

# X for Rock, 
# Y for Paper
# Z for scissors

# X means you need to lose, 
# Y means you need to end the round in a draw
# Z means you need to win. Good luck!"



hand = {'A': 1, 'B': 2, 'C': '3', 'X': 1, 'Y': 2, 'Z': 3}
volgorde = [3,1,2,3,1]
score = 0
for x in t:
    p1 = int(hand[x[0]])
    
    # bepaal hand
    if x[1] == 'X': #lose
        p2 = volgorde[p1-1]
    elif x[1] == 'Y':
        p2 = p1
    else:
        p2 = volgorde[p1+1]

    #bereken score
    if p1 == p2:
        score += p2 + 3
    elif p1 == 3 and p2 == 2:
        score += p2
    elif p1 == 3 and p2 == 1:
        score += p2 + 6
    elif p1 == 2 and p2 == 3:
        score += p2 + 6
    elif p1 == 2 and p2 == 1:
        score += p2
    elif p1 == 1 and p2 == 3:
        score += p2
    elif p1 == 1 and p2 == 2:
        score += p2 + 6
    else: 
        print (f'error {p1} {p2} {p1==p2}')
    print(score, p1, p2)

print (score)

runtime  = datetime.datetime.now() - time
print (runtime)
