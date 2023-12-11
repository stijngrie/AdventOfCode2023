
file1 = open('Day8/Day8-Input.txt', 'r')
Lines = file1.readlines()

moves = Lines[0].replace("\n", "")
map = dict()
position = "AAA"

Lines.pop(0)
Lines.pop(0)
for line in Lines:
    start = line.split("=")[0].replace(" ", "")
    ends = line.replace("\n", "").split("=")[1].replace(" ","").replace("(", "").replace(")", "").split(",")
    map[start] = ends
steps = 0
index = 0
while True:
    position = map[position][0 if moves[index] == "L" else 1]
    steps += 1
    if position == "ZZZ":
        break
    if index == len(moves)-1:
        index = 0
    else:
        index += 1
        
print(steps)
