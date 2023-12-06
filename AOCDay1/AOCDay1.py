f = open("Inputs\AOCday1-input.txt", "r")
#f = open("Inputs\AOCday1-sample.txt", "r")

# Declare array for summing
arr=[]

# Declare dictonary for translating text digits
numdict = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

for line in f:

    first=0
    wordbuilder=""
    # Parse left to right for first digit
    for char in line:        
        if first!=0:
            break   
        # If numeric, figure out location and set firstdigit var appropriately     
        if char.isnumeric():
            firstdigit = char
            first=1
            break                
        # If non-numeric, add to wordbuilder and check against dict
        else:
            wordbuilder+=char
            #print(wordbuilder)
            # check whole wordbuilder
            if wordbuilder in numdict:
                firstdigit = numdict.get(wordbuilder)
                first=1
                break
            # check all substrings of wordbuilder in case of leading chars
            else:   
                for x in range(1,len(wordbuilder)-1):
                    #print(wordbuilder[x:len(wordbuilder)])
                    if wordbuilder[x:len(wordbuilder)] in numdict:
                        firstdigit = numdict.get(wordbuilder[x:len(wordbuilder)])
                        first=1
                        break

    #print(firstdigit)

    last=0
    wordbuilder=""
    line = line[::-1]
    #print("Line: "+line)
    for char in line:        
        if last!=0:
            break   
        # If numeric, figure out location and set firstdigit var appropriately     
        #print("Char: "+char)
        if char.isnumeric():
            lastdigit = char
            last=1
            break                
        # If non-numeric, add to wordbuilder and check against dict
        else:
            wordbuilder+=char
            revwordbuilder = wordbuilder[::-1]
            # print(wordbuilder)
            # print(revwordbuilder)
            # check whole wordbuilder
            if revwordbuilder in numdict:
                lastdigit = numdict.get(revwordbuilder)
                last=1
                break
            # check all substrings of wordbuilder in case of leading chars
            else:   
                for x in range(1,len(revwordbuilder)):
                    #print(wordbuilder[x:len(wordbuilder)])                    
                    if revwordbuilder[0:len(revwordbuilder)-x] in numdict:
                        lastdigit = numdict.get(revwordbuilder[0:len(revwordbuilder)-x])
                        last=1
                        break
    # print("firstdigit: "+firstdigit)
    # print("lastdigit: "+lastdigit)
     
    arr.append(int(firstdigit+lastdigit))
    #print(line)

sum=0
cnt=1
for x in arr:
    print("Line: "+str(cnt)+" Value: "+str(x))
    sum += x
    cnt+=1

print(sum)
