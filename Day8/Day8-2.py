import math

file1 = open('Day8/Day8-Input.txt', 'r')
Lines = file1.readlines()

moves = Lines[0].replace("\n", "")
map = dict()
positions = []
endzones = []
startzones = []

Lines.pop(0)
Lines.pop(0)
for line in Lines:
    start = line.split("=")[0].replace(" ", "")
    if start.endswith("A"):
        positions.append(start)
    ends = line.replace("\n", "").split("=")[1].replace(" ","").replace("(", "").replace(")", "").split(",")
    map[start] = ends

for position in positions:
    startzones.append(position)
    endzones.append([])

for index, position in enumerate(positions):
    temppos = position
    steps = 0
    ended = False
    firstZ = None
    while ended == False:
        for move in moves:
            steps += 1
            temppos = map[temppos][0 if move == "L" else 1]
            if temppos.endswith("Z"):
                endzones[index].append(steps)
                if firstZ == None:
                    steps = 0
                    firstZ = temppos
                elif temppos == firstZ:
                    ended = True
                    break

numbers = [endzone[0] for endzone in endzones]
answer = math.lcm(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5])
print(answer)