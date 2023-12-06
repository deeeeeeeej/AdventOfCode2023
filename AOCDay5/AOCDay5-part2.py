import re

#################
### Functions ###
#################
def parse_input(element):
    
    seeds_pattern = re.compile(r'seeds:')
    match = seeds_pattern.match(element)
    if match is not None:
        print("Creating seeds...")
        element = re.split('\s',element)
        for i in range(1,len(element),2):   
            seedRanges.append(range(int(element[i]), int(element[i])+int(element[i+1])-1))        
        return

    seed_soil_pattern = re.compile(r'seed-to-soil map:')
    match = seed_soil_pattern.match(element)
    if match is not None:
        print("Mapping soil...")
        element = re.split('\n',element)
        for i in range(1,len(element)):
            vals = re.split(' ',element[i])
            seed_soil.append((range(int(vals[1]),int(vals[1])+int(vals[2])-1),int(vals[0])-(int(vals[1]))))        
        return

    soil_fertilizer_pattern = re.compile(r'soil-to-fertilizer map:')
    match = soil_fertilizer_pattern.match(element)
    if match is not None:
        print("Mapping fertilizer...")
        element = re.split('\n',element)
        for i in range(1,len(element)):
            vals = re.split(' ',element[i])
            soil_fertilizer.append((range(int(vals[1]),int(vals[1])+int(vals[2])-1),int(vals[0])-(int(vals[1]))))
        return

    fertilizer_water_pattern = re.compile(r'fertilizer-to-water map:')
    match = fertilizer_water_pattern.match(element)
    if match is not None:
        print("Mapping water...")
        element = re.split('\n',element)
        for i in range(1,len(element)):
            vals = re.split(' ',element[i])
            fertilizer_water.append((range(int(vals[1]),int(vals[1])+int(vals[2])-1),int(vals[0])-(int(vals[1]))))            
        return

    water_light_pattern = re.compile(r'water-to-light map:')
    match = water_light_pattern.match(element)
    if match is not None:
        print("Mapping light...")
        element = re.split('\n',element)
        for i in range(1,len(element)):
            vals = re.split(' ',element[i])
            water_light.append((range(int(vals[1]),int(vals[1])+int(vals[2])-1),int(vals[0])-(int(vals[1]))))
        return

    light_temperature_pattern = re.compile(r'light-to-temperature map:')
    match = light_temperature_pattern.match(element)
    if match is not None:
        print("Mapping temperature...")
        element = re.split('\n',element)
        for i in range(1,len(element)):
            vals = re.split(' ',element[i])
            light_temperature.append((range(int(vals[1]),int(vals[1])+int(vals[2])-1),int(vals[0])-(int(vals[1]))))
        return

    temperature_humidity_pattern = re.compile(r'temperature-to-humidity map:')
    match = temperature_humidity_pattern.match(element)
    if match is not None:
        print("Mapping humidity...")
        element = re.split('\n',element)
        for i in range(1,len(element)):
            vals = re.split(' ',element[i])
            temperature_humidity.append((range(int(vals[1]),int(vals[1])+int(vals[2])-1),int(vals[0])-(int(vals[1]))))
        return

    humidity_location_pattern = re.compile(r'humidity-to-location map:')
    match = humidity_location_pattern.match(element)
    if match is not None:
        print("Mapping location...")
        element = re.split('\n',element)
        for i in range(1,len(element)):
            vals = re.split(' ',element[i])
            humidity_location.append((range(int(vals[1]),int(vals[1])+int(vals[2])-1),int(vals[0])-(int(vals[1]))))
        return

def compare_ranges(range1List, range2List):

    for range1 in range1List:

        xmin = min(range1)
        xmax = max(range1)

        for range2 in range2List:

            ymin = min(range2[0])
            ymax = max(range2[0])
            offset = range2[1]

            # No overlap
            if(xmax < ymin or ymax < xmin):
                print("No overlap.")
            elif (xmin <= ymax and ymin <= xmax):
                print("Overlap.")

# Open file
f = open("AOCDay5/AOCday5-sample.txt", "r")
#f = open("AOCDay5/AOCday5-input.txt", "r")

# Get data into format for later parsing
f = f.read()
f = (re.split('\n\n', f))

seedRanges = []
seed_soil = []
soil_fertilizer = []
fertilizer_water = []
water_light = []
light_temperature = []
temperature_humidity = []
humidity_location = []

for element in f:

    parse_input(element)

print(seedRanges)
print(seed_soil)
compare_ranges(seedRanges, seed_soil)
print(soil_fertilizer)
print(fertilizer_water)
print(water_light)
print(light_temperature)
print(temperature_humidity)
print(humidity_location)
minLocation = -1

