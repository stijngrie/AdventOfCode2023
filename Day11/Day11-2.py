from dataclasses import dataclass

@dataclass
class Galaxy:
    x: int
    y: int
file1 = open('Day11/Day11-Input.txt', 'r')
Lines = file1.readlines()
galaxies = []
lineNums = list(range(0, len(Lines)))
rowNums = list(range(0, len(Lines[0])-1))
answer = 0
emptySpace = 1000000

for y, line in enumerate(Lines):
    line = line.replace("\n", "")
    for x, char in enumerate(line):
        if char == "#":
            galaxies.append(Galaxy(x=x, y=y))
            if y in lineNums:
                lineNums.remove(y)
            if x in rowNums:
                rowNums.remove(x)

for index, galaxy in enumerate(galaxies):
    for galaxy2 in galaxies[:index]:
        for row in range(min(galaxy.x, galaxy2.x), max(galaxy.x, galaxy2.x)):
            if row in rowNums:
                answer += emptySpace
            else:
                answer += 1
        for column in range(min(galaxy.y, galaxy2.y), max(galaxy.y, galaxy2.y)):
            if column in lineNums:
                answer += emptySpace
            else:
                answer += 1
print(answer)
