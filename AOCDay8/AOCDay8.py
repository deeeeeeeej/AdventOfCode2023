import re
from math import lcm

# Open file
#f = open("Inputs/AOCday8-sample.txt", "r")
f = open("Inputs/AOCday8-input.txt", "r")

def parse(line):

    x = re.split('=',line)
    y = x[1].replace('(','').replace(')','').split(',')
    mapDict[x[0].strip()] = (y[0].strip(), y[1].strip())

    return 0

# Part 1
def getDistance(startStep, pattern):

    step = startStep
    counter = 0
    # Remove [2] from step for part 1
    while step != 'ZZZ':

        for i in pattern:
            step = explore(step, int(i))
            counter+=1

    return counter


# Part 2
def getMinDistance(startStep, pattern):

    step = startStep
    counter = 0
    while step[2] != 'Z':

        for i in pattern:
            step = explore(step, int(i))
            counter+=1

    return counter

def explore(key, direction):

    return mapDict[key][direction]

mapDict = {}

f = f.read().strip()
f = (re.split('\n\n', f))

pattern = f[0]
pattern = pattern.replace('L','0')
pattern = pattern.replace('R','1')

for line in re.split('\n', f[1]):
    parse(line)

# Part 1 Output
#print(getDistance('AAA', pattern))

minDistances = []
# Part 2 Output
for starts in mapDict.keys():

    if starts[2] == 'A':
        minDistances.append(getMinDistance(starts,pattern))


print(lcm(*minDistances))
