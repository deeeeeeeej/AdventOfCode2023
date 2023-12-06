import re

#f = open("Inputs/AOCday4-sample.txt", "r")
f = open("Inputs/AOCday4-input.txt", "r")

f = f.readlines()

def calc_score(line):
    
    # initial split on colon
    line = re.split(': ', line)
    cardNum_pattern = re.compile(r'Card\s+(?P<gameNum>\d+)')
    match = cardNum_pattern.match(line[0])

    #extract gameNum from line
    cardNum = match.group(1)
    #print("Card " + str(cardNum))

    if str(cardNum) in cardDict.keys():
        cardDict[str(cardNum)] += 1
        #print("Added to cardDict["+str(cardNum)+"]. New value: "+str(cardDict[str(cardNum)]))
    else:
        cardDict[str(cardNum)] = 1
        #print("Created new entry in cardDict: "+str(cardNum))

    # secondary split on each grab
    line_games = re.split('\| ',line[1])
    winningNumbers = re.split('\s+',line_games[0].strip())
    gameNumbers = re.split('\s+', line_games[1].strip())

    # calc score
    gameScore = 0
    for game in gameNumbers:
        if game in winningNumbers:
            if gameScore == 0:
                gameScore = 1
            else:
                # Part 1 Math
                #gameScore = gameScore*2
                # Part 2 Math
                gameScore += 1

    #print("Score: " + str(gameScore))
    update_scratchers(int(cardNum), gameScore)

def update_scratchers(cardNum, cardScore):
    
    for x in range(cardDict[str(cardNum)]):
        for i in range(1,cardScore+1):
            #print(i)
            #print(cardNum+i)
            if str(cardNum+i) in cardDict.keys():
                cardDict[str(cardNum+i)] += 1
                #print("Added to cardDict["+str(cardNum+i)+"]. New value: "+str(cardDict[str(cardNum+i)]))
            else:
                cardDict[str(cardNum+i)] = 1
                #print("Created new entry in cardDict: "+str(cardNum+i))

cardDict = {}
totalCards=0
for line in f:

    calc_score(line)

for card in cardDict.keys():
    totalCards += cardDict[card]

print(totalCards)