from dataclasses import dataclass

file1 = open('Day5/Day5-InputT.txt', 'r')
Lines = file1.readlines()

@dataclass
class Map:
    destinationStart: int
    sourceStart: int
    range: int

seeds = []
seedToSoilD = []
soilToFertilizerD = []
fertilizerToWaterD = []
waterToLightD = []
lightToTempD = []
tempToHumidD = []
humidToLocationD = []

mode = 0

for line in Lines:
    line = line.replace("\n", "")
    tempMap = ''
    
    # Get the map
    if len(line) > 0:
        if line[0].isnumeric():
            tempMap = Map(int(line.split(" ")[0]), int(line.split(" ")[1]), int(line.split(" ")[2]))
        
        # Get seeds
        if line.startswith("seeds"):
            seeds = line.split(": ")[1].split(" ")
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
    
    def Translate(source: int, maps: []):
        for map in maps:
            if source >= map.sourceStart and source < map.sourceStart + map.range:
                return source - map.sourceStart + map.destinationStart
        return source
       
locations = []     
for seed in seeds:
    locations.append(Translate(Translate(Translate(Translate(Translate(Translate(Translate(int(seed), seedToSoilD), soilToFertilizerD), fertilizerToWaterD), waterToLightD), lightToTempD), tempToHumidD), humidToLocationD))
locations.sort()

print(Translate(Translate(Translate(55, seedToSoilD), soilToFertilizerD), fertilizerToWaterD))
print(Translate(Translate(Translate(67, seedToSoilD), soilToFertilizerD), fertilizerToWaterD))


# print(locations[0])