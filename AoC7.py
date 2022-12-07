import pathlib
import datetime
import os
from anytree import Node, RenderTree

time = datetime.datetime.now() 
os.chdir('./Advent of Code/2022/Advent-of-Code-2022')

SCORE = 0

with open("AoC7.txt", encoding='UTF-8') as f:
    t = f.readlines()

commandline = [x.strip() for x in t]

def scanFiles(path):
    global SCORE
    dirSize = 0 
    for item in path.children:
        if item.type == 'dir':
            item.size = scanFiles(item)
        dirSize += int(item.size)
    if dirSize <= 100000:
        SCORE += dirSize
    return dirSize

filesystem = {'':''}
filesystem[''] = Node('', parent=None, size=0)
rootNode = filesystem['']
currentDir = filesystem['']

for idx, line in enumerate(commandline):
    line = line.split(' ')
    if line[0] == '$': 
        if line[1] == 'cd':
            if line[2] == '..':
                #if currentDir.is_root:
                #    filesystem.append(Node('/'))
                #    currentDir.parent = filesystem[-1]
                #    rootNode = filesystem[-1]    
                currentDir = currentDir.parent
            elif line[2] == '/':
                currentDir = rootNode
            else:
                currentDir = filesystem[currentDir.name + line[2]]         
    elif line[0] == 'dir':
            filesystem[currentDir.name + line[1]] = Node(name=line[1], size=0, type='dir', parent=currentDir)
    elif line[0] != '$':
            filesystem[currentDir.name + line[1]] = Node(name=line[1], size=line[0], type='file', parent=currentDir)

filesystem[''].size = int(scanFiles(filesystem['']))

#print (RenderTree(filesystem['']))

#print(filesize)
#print(SCORE)
neededSpace = (30000000 - (70000000 - filesystem[''].size))
print (min([int(filesystem[item].size) for item in filesystem if int(filesystem[item].size) > neededSpace]))
   
        
runtime  = datetime.datetime.now() - time
print (runtime)