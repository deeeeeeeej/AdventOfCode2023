
f = open("Inputs/AOCday2-sample.txt", "r")
#f = open("Inputs/AOCday2-input.txt", "r")

import re

maxDict = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def game_isValid(line):

    isValid=True

    # initial split on colon
    line = re.split(': ', line)
    gameNum_pattern = re.compile(r'Game\s(?P<gameNum>\d+)')
    match = gameNum_pattern.match(line[0])
    
    #extract gameNum from line
    gameNum = match.group(1)
    
    # secondary split on each grab
    line_games = re.split('; ',line[1])
    print(line_games)
    
    grab_pattern = re.compile(r'(?P<val>\d+)\s(?P<color>\w+)')
    
    for grab in line_games:
        #split for each individual color in each grab
        for color in re.split(', ',grab):
            grabmatch = grab_pattern.match(color)
            if int(grabmatch.group(1)) > maxDict[grabmatch.group(2)]:
                isValid=0
    
    if (isValid):
        return int(gameNum)
    else: 
        return 0



    # If game is valid, return gameNum, else return 0

gameDict = {}
sum=0 

for line in f:
   
    #print(line.split(': '))
    sum+=game_isValid(line)

print(sum)