import pathlib
import datetime
import os
time = datetime.datetime.now() 
os.chdir('./Advent of Code/2022/Advent-of-Code-2022')

score = 0

with open("AoC6.txt", encoding='UTF-8') as f:
    t = f.readlines()

t = t[0]

#t = 'bvwbjplbgvbhsrlpgdmjqwftvncz' #: first marker after character 5
#t  = 'nppdvjthqldpwncqszvftbrmjlhg' #: first marker after character 6
#t = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' #: first marker after character 10
#t = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' #: first marker after character 11

for x in range(13,len(t)):
    token = set([x for x in t[x-13:x+1]])

    if len(token) == 14:
        print (t[x-13:x+1], t[x], x+1)
        break

#print (t)
#print(score)
        
runtime  = datetime.datetime.now() - time
print (runtime)