
#f = open("Inputs/AOCday2-sample.txt", "r")
f = open("Inputs/AOCday2-input.txt", "r")

import re

def game_isValid(line):

    isValid=True

    # initial split on colon
    line = re.split(': ', line)
    
    # secondary split on each grab
    line_games = re.split('; ',line[1])
    print(line_games)
    
    grab_pattern = re.compile(r'(?P<val>\d+)\s(?P<color>\w+)')
    
    maxDict = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for grab in line_games:
        #split for each individual color in each grab
        for color in re.split(', ',grab):
            grabmatch = grab_pattern.match(color)
            if int(grabmatch.group(1)) > maxDict[grabmatch.group(2)]:
                maxDict[grabmatch.group(2)] = int(grabmatch.group(1))

    power = 1
    for i in maxDict:
        power = power * maxDict[i]

    return power


sum=0 

for line in f:
   
    #print(line.split(': '))
    sum+=game_isValid(line)

print(sum)