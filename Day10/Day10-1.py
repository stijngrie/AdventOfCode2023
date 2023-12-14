from dataclasses import dataclass

file1 = open('Day10/Day10-Input.txt', 'r')
Lines = file1.readlines()

@dataclass
class Pipe:
    startPos: str
    positions: []
    steps: int
    direction: str

startLocation = 0
startPipes = []
for y, line in enumerate(Lines):
    for x, char in enumerate(line):
        if char == "S":
            startLocation = str(x) + "," + str(y)
            # Check what pipes connect
            # Left
            if x - 1 > 0:
                if Lines[y][x-1] == "-":
                    startPipes.append(Pipe(str(x-1) + "," + str(y), [], 1, "L"))
                elif Lines[y][x-1] == "L":
                    startPipes.append(Pipe(str(x-1) + "," + str(y), [], 1, "U"))
                elif Lines[y][x-1] == "F":
                    startPipes.append(Pipe(str(x-1) + "," + str(y), [], 1, "D"))
            # Right
            if x + 1 < len(line):
                if Lines[y][x+1] == "-":
                    startPipes.append(Pipe(str(x+1) + "," + str(y), [], 1, "R"))
                elif Lines[y][x+1] == "J":
                    startPipes.append(Pipe(str(x+1) + "," + str(y), [], 1, "U"))
                elif Lines[y][x+1] == "7":
                    startPipes.append(Pipe(str(x+1) + "," + str(y), [], 1, "D"))
            # Up
            if y - 1 > 0:
                if Lines[y-1][x] == "|":
                    startPipes.append(Pipe(str(x) + "," + str(y-1), [], 1, "U"))
                elif Lines[y-1][x] == "F":
                    startPipes.append(Pipe(str(x) + "," + str(y-1), [], 1, "R"))         
                elif Lines[y-1][x] == "7":
                    startPipes.append(Pipe(str(x) + "," + str(y-1), [], 1, "L"))
            # Down
            if y + 1 < len(Lines):
                if Lines[y+1][x] == "|":
                    startPipes.append(Pipe(str(x) + "," + str(y+1), [], 1, "D"))          
                elif Lines[y+1][x] == "J":
                    startPipes.append(Pipe(str(x) + "," + str(y+1), [], 1, "L"))
                elif Lines[y+1][x] == "L":
                    startPipes.append(Pipe(str(x) + "," + str(y+1), [], 1, "R"))
            break
for pipe in startPipes:
    pipe.positions.append(pipe.startPos)


# Go in direction of pipes
connected = False
while connected == False:
    for pipe in startPipes:
        # Get last positions
        x = int(pipe.positions[-1].split(",")[0])
        y = int(pipe.positions[-1].split(",")[1])
        # Left
        if pipe.direction == "L":
            if Lines[y][x-1] == "-":
                pipe.direction = "L"
                pipe.positions.append(str(x-1) + "," + str(y))
                pipe.steps += 1
            elif Lines[y][x-1] == "L":
                pipe.direction = "U"
                pipe.positions.append(str(x-1) + "," + str(y))
                pipe.steps += 1
            elif Lines[y][x-1] == "F":
                pipe.direction = "D"
                pipe.positions.append(str(x-1) + "," + str(y))
                pipe.steps += 1
        # Right
        elif pipe.direction == "R":
            if Lines[y][x+1] == "-":
                pipe.direction = "R"
                pipe.positions.append(str(x+1) + "," + str(y))
                pipe.steps += 1
            elif Lines[y][x+1] == "J":
                pipe.direction = "U"
                pipe.positions.append(str(x+1) + "," + str(y))
                pipe.steps += 1
            elif Lines[y][x+1] == "7":
                pipe.direction = "D"
                pipe.positions.append(str(x+1) + "," + str(y))
                pipe.steps += 1
        # Up
        elif pipe.direction == "U":
            if Lines[y-1][x] == "|":
                pipe.direction = "U"
                pipe.positions.append(str(x) + "," + str(y-1))
                pipe.steps += 1
            elif Lines[y-1][x] == "F":
                pipe.direction = "R"
                pipe.positions.append(str(x) + "," + str(y-1))
                pipe.steps += 1      
            elif Lines[y-1][x] == "7":
                pipe.direction = "L"
                pipe.positions.append(str(x) + "," + str(y-1))
                pipe.steps += 1
        # Down
        elif pipe.direction == "D":
            if Lines[y+1][x] == "|":
                pipe.direction = "D"
                pipe.positions.append(str(x) + "," + str(y+1))
                pipe.steps += 1       
            elif Lines[y+1][x] == "J":
                pipe.direction = "L"
                pipe.positions.append(str(x) + "," + str(y+1))
                pipe.steps += 1       
            elif Lines[y+1][x] == "L":
                pipe.direction = "R"
                pipe.positions.append(str(x) + "," + str(y+1))
                pipe.steps += 1    
        connectWithOther = False   
        for tPipe in startPipes:
            if tPipe != pipe:
                if pipe.positions[-1] in tPipe.positions:
                    connected = True
                    break
print(startPipes[0].steps)