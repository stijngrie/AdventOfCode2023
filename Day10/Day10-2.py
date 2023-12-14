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
maybe_s = {"-", "|", "F", "J", "7", "L"}
for y, line in enumerate(Lines):
    for x, char in enumerate(line):
        if char == "S":
            startLocation = str(x) + "," + str(y)
            # Check what pipes connect
            # Left
            if x - 1 > 0:
                if Lines[y][x-1] == "-":
                    startPipes.append(Pipe(str(x-1) + "," + str(y), [], 1, "L"))
                    maybe_s &= {"J", "-", "7"}
                elif Lines[y][x-1] == "L":
                    startPipes.append(Pipe(str(x-1) + "," + str(y), [], 1, "U"))
                    maybe_s &= {"J", "-", "7"}
                elif Lines[y][x-1] == "F":
                    startPipes.append(Pipe(str(x-1) + "," + str(y), [], 1, "D"))
                    maybe_s &= {"J", "-", "7"}
            # Right
            if x + 1 < len(line):
                if Lines[y][x+1] == "-":
                    startPipes.append(Pipe(str(x+1) + "," + str(y), [], 1, "R"))
                    maybe_s &= {"L", "-", "F"}
                elif Lines[y][x+1] == "J":
                    startPipes.append(Pipe(str(x+1) + "," + str(y), [], 1, "U"))
                    maybe_s &= {"L", "-", "F"}
                elif Lines[y][x+1] == "7":
                    startPipes.append(Pipe(str(x+1) + "," + str(y), [], 1, "D"))
                    maybe_s &= {"L", "-", "F"}
            # Up
            if y - 1 > 0:
                if Lines[y-1][x] == "|":
                    startPipes.append(Pipe(str(x) + "," + str(y-1), [], 1, "U"))
                    maybe_s &= {"|", "J", "L"}
                elif Lines[y-1][x] == "F":
                    startPipes.append(Pipe(str(x) + "," + str(y-1), [], 1, "R")) 
                    maybe_s &= {"|", "J", "L"}        
                elif Lines[y-1][x] == "7":
                    startPipes.append(Pipe(str(x) + "," + str(y-1), [], 1, "L"))
                    maybe_s &= {"|", "J", "L"}
            # Down
            if y + 1 < len(Lines):
                if Lines[y+1][x] == "|":
                    startPipes.append(Pipe(str(x) + "," + str(y+1), [], 1, "D"))
                    maybe_s &= {"|", "7", "F"}          
                elif Lines[y+1][x] == "J":
                    startPipes.append(Pipe(str(x) + "," + str(y+1), [], 1, "L"))
                    maybe_s &= {"|", "7", "F"}  
                elif Lines[y+1][x] == "L":
                    startPipes.append(Pipe(str(x) + "," + str(y+1), [], 1, "R"))
                    maybe_s &= {"|", "7", "F"}  
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

# Combine all used positions
pipePos = startPipes[0].positions + startPipes[1].positions
options = ["7", "F", "L", "J", "|", "-"]
# Set start position to actual pipe segment
for y, line in enumerate(Lines):
    for x, char in enumerate(line):
        if char in options:
            if str(x) + "," + str(y) not in pipePos:
                Lines[y] = Lines[y][:x] + "." + Lines[y][x + 1:] 

answer = 0
openPipe = False
file2 = open('Day10/Day10-InputOUT.txt', 'w')
text = ""
down = False
up = False
for y, lineT in enumerate(Lines):
    line = lineT.replace("\n", "").replace("S", list(maybe_s)[0])
    for x, char in enumerate(line):
        if char == "|":
            openPipe = not openPipe
            text = text + char
            down = False
            up = False
        elif char == "F":
            down = True
            text = text + char
        elif char == "7":
            if up:
                openPipe = not openPipe
            down = False
            up = False
            text = text + char
        elif char == "L":
            up = True
            text = text + char
        elif char == "J":
            if down:
                openPipe = not openPipe
            down = False
            up = False
            text = text + char
        else:
            if openPipe and char != "-":
                text = text + "W"
                answer += 1
            else:
                text = text + char
    text = text + "\n"
file2.write(text)
print(answer)