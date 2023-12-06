import sys
import re

######################
### Object Classes ###
######################
class Seed:
    def __init__(self, seedNo):
        self.seedNo = seedNo
        self.soil = -1
        self.fertilizer = -1
        self.water = -1
        self.light = -1
        self.temperature = -1
        self.humidity = -1
        self.location = -1

    def toStr(self):
        print("Seed "+str(self.seedNo)+", soil "+str(self.soil)+", fertilizer "+str(self.fertilizer)+", water "+str(self.water)+", light "+str(self.light)+", temperature "+str(self.temperature)+", humidity "+str(self.humidity)+", location "+str(self.location))

#################
### Functions ###
#################
def parse_input(element):

    #Check which map this is
    #Commenting out for part 2
    seeds_pattern = re.compile(r'seeds:')
    match = seeds_pattern.match(element)
    if match is not None:
        print("Creating seeds...")
        element = re.split('\s',element)
        for i in range(1,len(element)):
            s = Seed(int(element[i]))
            seedList.append(s)
        return
    


    seed_soil_pattern = re.compile(r'seed-to-soil map:')
    match = seed_soil_pattern.match(element)
    if match is not None:
        print("Mapping soil...")
        element = re.split('\n',element)
        for i in range(1,len(element)):
            vals = re.split(' ',element[i])
            map_soil(int(vals[0]), int(vals[1]), int(vals[2]))
        return

    soil_fertilizer_pattern = re.compile(r'soil-to-fertilizer map:')
    match = soil_fertilizer_pattern.match(element)
    if match is not None:
        print("Mapping fertilizer...")
        element = re.split('\n',element)
        for i in range(1,len(element)):
            vals = re.split(' ',element[i])
            map_fertilizer(int(vals[0]), int(vals[1]), int(vals[2]))
        return

    fertilizer_water_pattern = re.compile(r'fertilizer-to-water map:')
    match = fertilizer_water_pattern.match(element)
    if match is not None:
        print("Mapping water...")
        element = re.split('\n',element)
        for i in range(1,len(element)):
            vals = re.split(' ',element[i])
            map_water(int(vals[0]), int(vals[1]), int(vals[2]))
        return

    water_light_pattern = re.compile(r'water-to-light map:')
    match = water_light_pattern.match(element)
    if match is not None:
        print("Mapping light...")
        element = re.split('\n',element)
        for i in range(1,len(element)):
            vals = re.split(' ',element[i])
            map_light(int(vals[0]), int(vals[1]), int(vals[2]))
        return

    light_temperature_pattern = re.compile(r'light-to-temperature map:')
    match = light_temperature_pattern.match(element)
    if match is not None:
        print("Mapping temperature...")
        element = re.split('\n',element)
        for i in range(1,len(element)):
            vals = re.split(' ',element[i])
            map_temperature(int(vals[0]), int(vals[1]), int(vals[2]))
        return

    temperature_humidity_pattern = re.compile(r'temperature-to-humidity map:')
    match = temperature_humidity_pattern.match(element)
    if match is not None:
        print("Mapping humidity...")
        element = re.split('\n',element)
        for i in range(1,len(element)):
            vals = re.split(' ',element[i])
            map_humidity(int(vals[0]), int(vals[1]), int(vals[2]))
        return

    humidity_location_pattern = re.compile(r'humidity-to-location map:')
    match = humidity_location_pattern.match(element)
    if match is not None:
        print("Mapping location...")
        element = re.split('\n',element)
        for i in range(1,len(element)):
            vals = re.split(' ',element[i])
            map_location(int(vals[0]), int(vals[1]), int(vals[2]))
        return

def map_soil(destStart, sourceStart, rangeVal):
    #print("Processing Source "+str(sourceStart)+" and Dest "+str(destStart)+" with range "+str(rangeVal))

    for seed in seedList:
        if seed.soil == -1:
            seed.soil = seed.seedNo
        if seed.seedNo in range(sourceStart, sourceStart+rangeVal):
            seed.soil = (seed.seedNo-sourceStart)+destStart

def map_fertilizer(destStart, sourceStart, rangeVal):
    #print("Processing Source "+str(sourceStart)+" and Dest "+str(destStart)+" with range "+str(rangeVal))

    for seed in seedList:
        if seed.fertilizer == -1:
            seed.fertilizer = seed.soil        
        if seed.soil in range(sourceStart, sourceStart+rangeVal):
            seed.fertilizer = (seed.soil-sourceStart)+destStart

def map_water(destStart, sourceStart, rangeVal):
    #print("Processing Source "+str(sourceStart)+" and Dest "+str(destStart)+" with range "+str(rangeVal))

    for seed in seedList:
        if seed.water == -1:
            seed.water = seed.fertilizer        
        if seed.fertilizer in range(sourceStart, sourceStart+rangeVal):
            seed.water = (seed.fertilizer-sourceStart)+destStart

def map_light(destStart, sourceStart, rangeVal):
    #print("Processing Source "+str(sourceStart)+" and Dest "+str(destStart)+" with range "+str(rangeVal))

    for seed in seedList:
        if seed.light == -1:
            seed.light = seed.water        
        if seed.water in range(sourceStart, sourceStart+rangeVal):
            seed.light = (seed.water-sourceStart)+destStart

def map_temperature(destStart, sourceStart, rangeVal):
    #print("Processing Source "+str(sourceStart)+" and Dest "+str(destStart)+" with range "+str(rangeVal))

    for seed in seedList:
        if seed.temperature == -1:
            seed.temperature = seed.light        
        if seed.light in range(sourceStart, sourceStart+rangeVal):
            seed.temperature = (seed.light-sourceStart)+destStart

def map_humidity(destStart, sourceStart, rangeVal):
    #print("Processing Source "+str(sourceStart)+" and Dest "+str(destStart)+" with range "+str(rangeVal))

    for seed in seedList:
        if seed.humidity == -1:
            seed.humidity = seed.temperature        
        if seed.temperature in range(sourceStart, sourceStart+rangeVal):
            seed.humidity = (seed.temperature-sourceStart)+destStart

def map_location(destStart, sourceStart, rangeVal):
    #print("Processing Source "+str(sourceStart)+" and Dest "+str(destStart)+" with range "+str(rangeVal))

    for seed in seedList:
        if seed.location == -1:
            seed.location = seed.humidity        
        if seed.humidity in range(sourceStart, sourceStart+rangeVal):
            seed.location = (seed.humidity-sourceStart)+destStart


# Open file
f = open("Inputs/AOCday5-sample.txt", "r")
#f = open("Inputs/AOCday5-input.txt", "r")

# Get data into format for later parsing
f = f.read()
f = (re.split('\n\n', f))
seedList = []

for element in f:

    parse_input(element)

minLocation = -1
for seed in seedList:

    seed.toStr()
    if minLocation == -1:
        minLocation = seed.location
    elif seed.location < minLocation:
        minLocation = seed.location

print(minLocation)
