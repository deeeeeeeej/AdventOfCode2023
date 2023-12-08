import re

# Functions TBD

def scoreHand(hand):

    cardCount = {}
    for card in hand:
        if card not in cardCount.keys():
            cardCount[card] = 1
        else: 
            cardCount[card] += 1

    # For Part 2 only
    if('J' in cardCount.keys()):
        
        if cardCount['J'] == 5:
            return 7
        
        maxScore = 0
        for card in cardCount.keys():
            if card != 'J':
                jokerScore = scoreHand(hand.replace('J',card))
                if jokerScore > maxScore:
                    maxScore = jokerScore
        
        return maxScore
        
    else:
        match len(cardCount):
            # Five of a kind
            case 1:
                return 7
            # Four of a kind, full house
            case 2:
                if all(i < 4 for i in (iter(cardCount.values()))):
                    return 5
                else:
                    return 6
            # Three of a kind, two pair
            case 3:
                if all(i < 3 for i in (iter(cardCount.values()))):
                    return 3
                else:
                    return 4
            # Pair
            case 4:
                return 2
            # High card
            case 5:
                return 1
    
    return 0

# Sort Function
def rankHands(hand):
    rank = str(hand[2])
    for card in hand[0]:
        # Change order of string for part 2
        if "J23456789TQKA".index(card) < 10:
            rank += '0'+str("J23456789TQKA".index(card))
        else:    
            rank += str("J23456789TQKA".index(card))
            
    return int(rank)


# Open file
#f = open("Inputs/AOCday7-sample.txt", "r")
f = open("Inputs/AOCday7-input.txt", "r")

f = f.readlines()

pokerList = []

for line in f:

    hand = line.split()[0]
    bid = line.split()[1]
    score = scoreHand(hand)
    pokerList.append([hand, int(bid), score])
    
pokerList.sort(key=rankHands)

winnings = 0
for i,hand in enumerate(pokerList,1):
    winnings += hand[1]*i
    #print(hand[1])
    #print(i)

print(pokerList)
print(winnings)

# Scores
# FiveofaKind = 7
# FourofaKind = 6
# FullHouse = 5
# ThreeofaKind = 4
# TwoPair = 3
# Pair = 2
# HighCard = 1