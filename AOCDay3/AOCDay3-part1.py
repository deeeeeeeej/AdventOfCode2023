
import re

#f = open("Inputs/AOCday3-sample.txt", "r")
f = open("Inputs/AOCday3-input.txt", "r")

f=f.readlines()

def isAdjacent(lineNum, startIndex, endIndex):
    
    print("Current Num Check: "+f[lineNum][startIndex:endIndex])
    symbol_pattern = re.compile(r'.*?[^0-9.].*?')  

    # Check line above for symbol
    print("Line Above Check: "+f[maintainBoundaries(lineNum-1,0,len(f)-1)][maintainBoundaries(startIndex-1,0,len(f[maintainBoundaries(lineNum-1,0,len(f)-1)])):maintainBoundaries(endIndex+1,0,len(f[maintainBoundaries(lineNum-1,0,len(f)-1)]))].strip())
    symbol_match = symbol_pattern.match(f[maintainBoundaries(lineNum-1,0,len(f)-1)][maintainBoundaries(startIndex-1,0,len(f[maintainBoundaries(lineNum-1,0,len(f)-1)])):maintainBoundaries(endIndex+1,0,len(f[maintainBoundaries(lineNum-1,0,len(f)-1)]))].strip()) 
    if symbol_match is not None:
        print("Matched " + f[lineNum][startIndex:endIndex] + " on line above.")
        return True
    
    #Check current line for symbol
    print("Current Line Check: "+f[lineNum][maintainBoundaries(startIndex-1,0,len(f[maintainBoundaries(lineNum,0,len(f)-1)])):maintainBoundaries(endIndex+1,0,len(f[maintainBoundaries(lineNum-1,0,len(f)-1)]))].strip())
    symbol_match = symbol_pattern.match(f[lineNum][maintainBoundaries(startIndex-1,0,len(f[maintainBoundaries(lineNum,0,len(f)-1)])):maintainBoundaries(endIndex+1,0,len(f[maintainBoundaries(lineNum-1,0,len(f)-1)]))].strip()) 
    if symbol_match is not None:
        print("Matched " + f[lineNum][startIndex:endIndex] + " on same line.")
        return True
    
    # Check line below for symbol
    print("Line Below Check: "+f[maintainBoundaries(lineNum+1,0,len(f)-1)][maintainBoundaries(startIndex-1,0,len(f[maintainBoundaries(lineNum+1,0,len(f)-1)])):maintainBoundaries(endIndex+1,0,len(f[maintainBoundaries(lineNum+1,0,len(f)-1)]))].strip())
    symbol_match = symbol_pattern.match(f[maintainBoundaries(lineNum+1,0,len(f)-1)][maintainBoundaries(startIndex-1,0,len(f[maintainBoundaries(lineNum+1,0,len(f)-1)])):maintainBoundaries(endIndex+1,0,len(f[maintainBoundaries(lineNum+1,0,len(f)-1)]))].strip()) 
    if symbol_match is not None:
        print("Matched " + f[lineNum][startIndex:endIndex] + " on line below.")
        return True
    
    print("No match for " + f[lineNum][startIndex:endIndex])

    return False

def maintainBoundaries(val, minLimit, maxLimit):
    if val < minLimit:
        return minLimit
    elif val > maxLimit:
        return maxLimit
    else: 
        return val

sum=0
for lineNum,line in enumerate(f):
    print(lineNum)
    print(line)

    num_pattern = re.compile(r'(?P<num>\d+)')
    match = num_pattern.finditer(line)

    if match is not None:        
        for num in match:
            #print(line.find(num))
            #print(len(num))
            #print(line[line.find(num):(line.find(num)+len(num))])
            # print(type(num))
            # print(num)
            # print(num.start())
            # print(num.end())
            if isAdjacent(lineNum, num.start(), num.end()):
                sum+=int(num.group())
    else: 
        print("No numbers found on line " + str(lineNum))

print(sum)