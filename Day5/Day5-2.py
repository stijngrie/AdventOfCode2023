from dataclasses import dataclass
import math
import time

startTime = time.time()

file1 = open('Day5/Day5-Input.txt', 'r')
Lines = file1.readlines()

@dataclass
class Map:
    destinationStart: int
    sourceStart: int
    range: int
    
@dataclass
class Ranges:
    start: int
    end: int

seeds = []
seedNums = []
seedToSoilD = []
soilToFertilizerD = []
fertilizerToWaterD = []
waterToLightD = []
lightToTempD = []
tempToHumidD = []
humidToLocationD = []

mode = 0

def convertRange(rangeA, maps: []):
    newRanges = []
    rangeConverted = False
    for map in maps:
        if rangeA.start >= map.sourceStart and rangeA.end <= map.sourceStart + map.range - 1:
            newRanges.append(Ranges(rangeA.start - map.sourceStart + map.destinationStart, rangeA.end - map.sourceStart + map.destinationStart))
            rangeConverted = True
        elif rangeA.start < map.sourceStart and rangeA.end > map.sourceStart + map.range - 1:
            # Before range
            newRanges = newRanges + convertRange(Ranges(rangeA.start, map.sourceStart - 1), maps)
            # Middle range
            newRanges.append(Ranges(map.destinationStart, map.destinationStart + map.range - 1))
            # End range
            newRanges = newRanges + convertRange(Ranges(map.sourceStart + map.range, rangeA.end), maps)
            rangeConverted = True
        elif rangeA.start < map.sourceStart and (rangeA.end >= map.sourceStart and rangeA.end <= map.sourceStart + map.range - 1):
            # Before range
            newRanges = newRanges + convertRange(Ranges(rangeA.start, map.sourceStart - 1), maps)
            # Between range
            newRanges.append(Ranges(map.destinationStart, rangeA.end - map.sourceStart + map.destinationStart))
            rangeConverted = True
        elif rangeA.end > map.sourceStart + map.range - 1 and (rangeA.start >= map.sourceStart and rangeA.start <= map.sourceStart + map.range - 1):
            # Between range
            newRanges.append(Ranges(rangeA.start - map.sourceStart + map.destinationStart, map.destinationStart + map.range - 1))
            # End range
            newRanges = newRanges + convertRange(Ranges(map.sourceStart + map.range, rangeA.end), maps)
            rangeConverted = True
    if rangeConverted == False:
        newRanges.append(rangeA)
    return newRanges

def Translate(ranges: [], maps: []):
    newRanges = []
    for rangeA in ranges:
        for r in convertRange(rangeA, maps):
            if r not in newRanges:
                newRanges.append(r)
    return newRanges



for line in Lines:
    line = line.replace("\n", "")
    tempMap = ''
    
    # Get the map
    if len(line) > 0:
        if line[0].isnumeric():
            tempMap = Map(int(line.split(" ")[0]), int(line.split(" ")[1]), int(line.split(" ")[2]))
        
        # Get seeds
        if line.startswith("seeds"):
            seedNums = line.split(": ")[1].split(" ")
        # Set mode if new section starts
        elif line.startswith("seed-to-soil"):
            mode = seedToSoilD
        elif line.startswith("soil-to-fertilizer"):
            mode = soilToFertilizerD
        elif line.startswith("fertilizer-to-water"):
            mode = fertilizerToWaterD
        elif line.startswith("water-to-light"):
            mode = waterToLightD
        elif line.startswith("light-to-temperature"):
            mode = lightToTempD
        elif line.startswith("temperature-to-humidity"):
            mode = tempToHumidD
        elif line.startswith("humidity-to-location"):
            mode = humidToLocationD

        # Add map to correct array
        elif mode == seedToSoilD:
            seedToSoilD.append(tempMap)
        elif mode == soilToFertilizerD:
            soilToFertilizerD.append(tempMap)
        elif mode == fertilizerToWaterD:
            fertilizerToWaterD.append(tempMap)
        elif mode == waterToLightD:
            waterToLightD.append(tempMap)
        elif mode == lightToTempD:
            lightToTempD.append(tempMap)
        elif mode == tempToHumidD:
            tempToHumidD.append(tempMap)
        elif mode == humidToLocationD:
            humidToLocationD.append(tempMap)

start = 1
seed = ""
for num in seedNums:
    if start == 1:
        seed = Ranges(int(num), 0)
        start *= -1
    elif start == -1:
        seed.end = int(seed.start) + (int(num)-1)
        seeds.append(seed)
        start *= -1
        seed = ""

answers = Translate(Translate(Translate(Translate(Translate(Translate(Translate(seeds, seedToSoilD), soilToFertilizerD), fertilizerToWaterD), waterToLightD), lightToTempD), tempToHumidD), humidToLocationD)
answer = math.inf
for test in answers:
    if test.start < answer:
        answer = test.start
print(answer)

endTime = time.time()
print("Elapsed time: ", round((endTime - startTime) * 1000, 1), "ms")