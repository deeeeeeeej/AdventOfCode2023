import re

# Open file
#f = open("Inputs/AOCday6-sample.txt", "r")
f = open("Inputs/AOCday6-input.txt", "r")

# Get data into format for later parsing
f = f.read().strip()
f = (re.split('\n\n', f))

# Parse input Part 1
t = f[0].split('\n')[0].split(':')[1].split()
d = f[0].split('\n')[1].split(':')[1].split()


# Part One functions
def getWinners(t, d):

    winners = 0
    for i in range(1,t):
        if i*(t-i) > d:
            winners += 1
    
    return winners

# Part 1 Answer
output = 1
for x in range(len(t)):
    output *= getWinners(int(t[x]), int(d[x]))

print("Part One Answer:", output)
        
# Parse input addition for Part 2
t = int(''.join(t))
d = int(''.join(d))

# Part Two functions
def getMinWinner(t, d):

    for i in range(1,t):
        if i*(t-i) > d:
            return i
        
def getMaxWinner(t, d):

    for i in reversed(range(1,t)):
        if i*(t-i) > d:
            return i
        

#Part Two Answer
print("Part Two Answer:", getMaxWinner(t,d) - getMinWinner(t,d)+1)